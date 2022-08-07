from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from rest_framework import status
from areas.models import Areas
from types_of_identity_documents.models import TypesOfIdentityDocuments
from employees.models import ThirdParties, Employees

from datetime import datetime
from dateutil.relativedelta import relativedelta

class RetrieveEmployeesViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):

        area = Areas.objects.create(
            description="Administration"
        )

        types_of_identity_documents = TypesOfIdentityDocuments.objects.create(
            code="CC",
            description='Citizenship Card'
        )

        third_party = ThirdParties.objects.create(
            identity_document="99999887",
            types_of_identity_documents=types_of_identity_documents,
            last_name="MONTOYA",
            second_surname='PEREZ',
            first_name='JUAN',
            middle_names='RUBEN',
            email='juan.montoya@cidenet.com.co'
        )

        employee = Employees.objects.create(
            third_party=third_party,
            country='CO',
            area=area,
            date_of_entry='2022-08-06 00:00:00'
        )

    def test_get_endpoint(self):
        client = APIClient()

        response = client.get('/api/employees')
        assert response.status_code == 200

    def test_get_endpoint_with_search_that_exists(self):
        client = APIClient()

        response = client.get('/api/employees?search=perez')
        assert response.status_code == 200

    def test_get_endpoint_with_search_that_does_not_exists(self):
        client = APIClient()

        response = client.get('/api/employees?search=ricardo')
        assert response.status_code == 200

class CreateEmployeesViewTest(RetrieveEmployeesViewTest):

    def test_post_endpoint(self):

        current_date = datetime.now()
        data = {
            'identity_document': '55556666',
            'last_name': 'JIMENEZ',
            'second_surname': 'RAMIREZ',
            'first_name': 'PAUL',
            'middle_names': 'DE LAS MONTANAS',
            'email': 'paul.jimenez@cidenet.com.us',
            'types_of_identity_documents_id': 1,
            'third_parties_employees':
                {
                    'country': 'US',
                    'date_of_entry': current_date,
                    'area_id': 1
                }
        }

        client = APIClient()
        response = client.post('/api/save-employees', data, format='json')

        assert response.status_code == 201

    def test_post_endpoint_send_repeated_data(self):

        current_date = datetime.now()
        data = {
            'identity_document': '99999887',
            'last_name': 'MONTOYA',
            'second_surname': 'RAMIREZ',
            'first_name': 'JUAN',
            'middle_names': 'RUBEN',
            'email': 'juan.montoyya@cidenet.com.us',
            'types_of_identity_documents_id': 1,
            'third_parties_employees':
                {
                    'country': 'US',
                    'date_of_entry': current_date,
                    'area_id': 1
                }
        }

        client = APIClient()
        response = client.post('/api/save-employees', data, format='json')

        assert response.status_code == 400


    def test_post_endpoint_send_invalid_data(self):

        current_date = datetime.now()
        data = {
            'identity_document': '99999884977',
            'last_name': 'cárdona',
            'second_surname': 'RAMIREZ',
            'first_name': 'Luis',
            'middle_names': 'RUBEN',
            'email': 'luis.cardona@cidenet.com.us',
            'types_of_identity_documents_id': 1,
            'third_parties_employees':
                {
                    'country': 'US',
                    'date_of_entry': current_date,
                    'area_id': 1
                }
        }

        client = APIClient()
        response = client.post('/api/save-employees', data, format='json')

        assert response.status_code == 400

    def test_post_endpoint_date_after_valida_range(self):

        date_after_valida_range = datetime.now() + relativedelta(days=1)
        data = {
            'identity_document': '88222594',
            'last_name': 'GARCIA',
            'second_surname': 'SOLARTE',
            'first_name': 'CARLOS',
            'middle_names': 'ALBERTO',
            'email': 'carlos.garcia@cidenet.com.co',
            'types_of_identity_documents_id': 1,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': date_after_valida_range,
                    'area_id': 1
                }
        }

        client = APIClient()
        response = client.post('/api/save-employees', data, format='json')

        assert response.status_code == 400

    def test_post_endpoint_date_before_valida_range(self):

        date_before_valida_range = datetime.now() - relativedelta(months=2)
        data = {
            'identity_document': '88222594',
            'last_name': 'GARCIA',
            'second_surname': 'SOLARTE',
            'first_name': 'CARLOS',
            'middle_names': 'ALBERTO',
            'email': 'carlos.garcia@cidenet.com.co',
            'types_of_identity_documents_id': 1,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': date_before_valida_range,
                    'area_id': 1
                }
        }

        client = APIClient()
        response = client.post('/api/save-employees', data, format='json')

        assert response.status_code == 400