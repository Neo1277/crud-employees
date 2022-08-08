from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from areas.models import Areas
from types_of_identity_documents.models import TypesOfIdentityDocuments
from employees.models import ThirdParties, Employees

from datetime import datetime
from dateutil.relativedelta import relativedelta


class RetrieveEmployeesViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.first_area = Areas.objects.create(
            description="Administration"
        )

        cls.first_types_of_identity_documents = TypesOfIdentityDocuments.objects.create(
            code="CC",
            description='Citizenship Card'
        )

        cls.first_third_party = ThirdParties.objects.create(
            identity_document="99999887",
            types_of_identity_documents=cls.first_types_of_identity_documents,
            last_name="MONTOYA",
            second_surname='PEREZ',
            first_name='JUAN',
            middle_names='RUBEN',
            email='juan.montoya@cidenet.com.co'
        )

        cls.first_employee = Employees.objects.create(
            third_party=cls.first_third_party,
            country='CO',
            area=cls.first_area,
            date_of_entry='2022-08-06 00:00:00'
        )

    def test_get_endpoint(self):
        response = self.client.get(reverse('retrieve-employeesview'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_endpoint_with_search_that_exists(self):
        response = self.client.get(reverse('retrieve-employeesview'), {'search': 'perez'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_endpoint_with_search_that_does_not_exists(self):
        response = self.client.get(reverse('retrieve-employeesview'), {'search': 'ricardo'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateEmployeesViewTest(RetrieveEmployeesViewTest):

    """
    @classmethod
    def setUpTestData(cls):
        super(CreateEmployeesViewTest, cls).setUpTestData()
    """

    def test_post_endpoint(self):

        current_date = datetime.now()
        data = {
            'identity_document': '55556666',
            'last_name': 'JIMENEZ',
            'second_surname': 'RAMIREZ',
            'first_name': 'PAUL',
            'middle_names': 'DE LAS MONTANAS',
            'email': 'paul.jimenez@cidenet.com.us',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'US',
                    'date_of_entry': current_date,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.post(reverse('save-employeesview'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_endpoint_send_repeated_data(self):

        current_date = datetime.now()
        invalid_data = {
            'identity_document': '99999887',
            'last_name': 'MONTOYA',
            'second_surname': 'RAMIREZ',
            'first_name': 'JUAN',
            'middle_names': 'RUBEN',
            'email': 'juan.montoya@cidenet.com.us',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'US',
                    'date_of_entry': current_date,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.post(reverse('save-employeesview'), invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_post_endpoint_send_invalid_data(self):

        current_date = datetime.now()
        invalid_data = {
            'identity_document': '99999884977',
            'last_name': 'cárdona',
            'second_surname': 'RAMIREZ',
            'first_name': 'Luis',
            'middle_names': 'RUBEN',
            'email': 'luis.cardona@cidenet.com.us',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'US',
                    'date_of_entry': current_date,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.post(reverse('save-employeesview'), invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_endpoint_date_after_valida_range(self):

        date_after_valida_range = datetime.now() + relativedelta(days=1)
        data = {
            'identity_document': '88222594',
            'last_name': 'GARCIA',
            'second_surname': 'SOLARTE',
            'first_name': 'CARLOS',
            'middle_names': 'ALBERTO',
            'email': 'carlos.garcia@cidenet.com.co',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': date_after_valida_range,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.post(reverse('save-employeesview'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_endpoint_date_before_valida_range(self):

        date_before_valida_range = datetime.now() - relativedelta(months=2)
        data = {
            'identity_document': '88222594',
            'last_name': 'GARCIA',
            'second_surname': 'SOLARTE',
            'first_name': 'CARLOS',
            'middle_names': 'ALBERTO',
            'email': 'carlos.garcia@cidenet.com.co',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': date_before_valida_range,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.post(reverse('save-employeesview'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
