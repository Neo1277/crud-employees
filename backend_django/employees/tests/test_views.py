from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from areas.models import Areas
from types_of_identity_documents.models import TypesOfIdentityDocuments
from employees.models import ThirdParties, Employees

from datetime import datetime
from dateutil.relativedelta import relativedelta

import json

"""
Correct way to make tests:
https://stackoverflow.com/q/60892321
"""
class RetrieveEmployeesViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.current_date = datetime.now()

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
            date_of_entry=cls.current_date
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
            'email': 'juan.montoya@cidenet.com.co',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'CO',
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
            'last_name': 'c??rdona',
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


class UpdateEmployeesViewTest(RetrieveEmployeesViewTest):

    @classmethod
    def setUpTestData(cls):
        super(UpdateEmployeesViewTest, cls).setUpTestData()

        cls.second_update_third_party = ThirdParties.objects.create(
            identity_document="999998874",
            types_of_identity_documents=cls.first_types_of_identity_documents,
            last_name="MONTOYA",
            second_surname='PEREZ',
            first_name='JUAN',
            middle_names='BERNARDO DE LOS RIOS',
            email='juan.montoya.1@cidenet.com.co'
        )

        cls.second_update_employee = Employees.objects.create(
            third_party=cls.second_update_third_party,
            country='CO',
            area=cls.first_area,
            date_of_entry=cls.current_date
        )

    def test_put_endpoint(self):

        current_date = datetime.now()
        data = {
            'identity_document': '999998874',
            'last_name': 'MONTOYA',
            'second_surname': 'CASTILLO',
            'first_name': 'JUAN',
            'middle_names': 'BERNARDO DE LOS RIOS',
            'email': 'juan.montoya.1@cidenet.com.co',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': current_date,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.put(
            reverse('update-employeesview', kwargs={'pk': self.second_update_third_party.pk}),
            data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_endpoint_send_repeated_data(self):

        current_date = datetime.now()
        invalid_data = {
            'identity_document': '99999887',
            'last_name': 'MONTOYA',
            'second_surname': 'RAMIREZ',
            'first_name': 'JUAN',
            'middle_names': 'RUBEN',
            'email': 'juan.montoya@cidenet.com.co',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': current_date,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.put(
            reverse('update-employeesview', kwargs={'pk': self.second_update_third_party.pk}),
            invalid_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_put_endpoint_send_invalid_data(self):

        current_date = datetime.now()
        invalid_data = {
            'identity_document': '999998849777',
            'last_name': 'c??rdona',
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

        response = self.client.put(
            reverse('update-employeesview', kwargs={'pk': self.second_update_third_party.pk}),
            invalid_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_endpoint_date_after_valida_range(self):

        date_after_valida_range = datetime.now() + relativedelta(days=1)
        data = {
            'identity_document': '999998874',
            'last_name': 'MONTOYA',
            'second_surname': 'CASTILLO',
            'first_name': 'JUAN',
            'middle_names': 'BERNARDO DE LOS RIOS',
            'email': 'juan.montoya.1@cidenet.com.co',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': date_after_valida_range,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.put(
            reverse('update-employeesview', kwargs={'pk': self.second_update_third_party.pk}),
            data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_endpoint_date_before_valida_range(self):

        date_before_valida_range = datetime.now() - relativedelta(months=2)
        data = {
            'identity_document': '999998874',
            'last_name': 'MONTOYA',
            'second_surname': 'CASTILLO',
            'first_name': 'JUAN',
            'middle_names': 'BERNARDO DE LOS RIOS',
            'email': 'juan.montoya.1@cidenet.com.co',
            'types_of_identity_documents_id': self.first_types_of_identity_documents.pk,
            'third_parties_employees':
                {
                    'country': 'CO',
                    'date_of_entry': date_before_valida_range,
                    'area_id': self.first_area.pk
                }
        }

        response = self.client.put(
            reverse('update-employeesview', kwargs={'pk': self.second_update_third_party.pk}),
            data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteEmployeesViewTest(RetrieveEmployeesViewTest):

    @classmethod
    def setUpTestData(cls):
        super(DeleteEmployeesViewTest, cls).setUpTestData()

        cls.second_delete_third_party = ThirdParties.objects.create(
            identity_document="888553451",
            types_of_identity_documents=cls.first_types_of_identity_documents,
            last_name="RIASCOS",
            second_surname='ORTIZ',
            first_name='KELLY',
            middle_names='JOHANA',
            email='kelly.riascos@cidenet.com.co'
        )

        cls.second_delete_employee = Employees.objects.create(
            third_party=cls.second_delete_third_party,
            country='CO',
            area=cls.first_area,
            date_of_entry=cls.current_date
        )

    def test_delete_endpoint(self):

        response = self.client.delete(
            reverse('delete-employeesview', kwargs={'pk': self.second_delete_third_party.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RetrieveNewEmailViewTest(RetrieveEmployeesViewTest):

    def test_retrieve_new_email_endpoint(self):

        parameters = {
            'last_name': 'BURBANO',
            'first_name': 'MARCELA',
            'country_code': 'US'
        }

        response = self.client.get(
            reverse('retrieve-new-email-employeesview',kwargs=parameters)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'email': 'marcela.burbano@cidenet.com.us'})

    def test_retrieve_new_email_endpoint_names_that_already_exist(self):

        parameters = {
            'last_name': 'MONTOYA',
            'first_name': 'JUAN',
            'country_code': 'US'
        }

        response = self.client.get(
            reverse('retrieve-new-email-employeesview',kwargs=parameters)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'email': 'juan.montoya.1@cidenet.com.us'})

    def test_retrieve_new_email_endpoint_with_pk_parameters_same_names(self):

        parameters = {
            'last_name': 'MONTOYA',
            'first_name': 'JUAN',
            'country_code': 'CO',
            'pk': self.first_third_party.pk
        }

        response = self.client.get(
            reverse('retrieve-new-email-employeesview',kwargs=parameters)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'email': 'juan.montoya@cidenet.com.co'})


    def test_retrieve_new_email_endpoint_with_pk_parameters_different_names(self):

        parameters = {
            'last_name': 'MENDEZ',
            'first_name': 'RAMIRO',
            'country_code': 'CO',
            'pk': self.first_third_party.pk
        }

        response = self.client.get(
            reverse('retrieve-new-email-employeesview',kwargs=parameters)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'email': 'ramiro.mendez@cidenet.com.co'})
