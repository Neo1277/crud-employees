# https://stackoverflow.com/a/51577650
# backend_django/types_of_identity_documents/management/commands/seed_types_of_identity_document.py
from django.core.management.base import BaseCommand

from types_of_identity_documents.models import TypesOfIdentityDocuments

import logging
logger = logging.getLogger(__name__)

# python manage.py seed --mode=refresh

""" Clear all data and creates types of identity document """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Types of identity document instances")
    TypesOfIdentityDocuments.objects.all().delete()

def create_type_of_identity_document(code: str, description: str):
    """Creates an area object with elements from the list"""

    type_of_identity_document = TypesOfIdentityDocuments(
        code=code,
        description=description,
    )
    type_of_identity_document.save()
    logger.info("{} Type of identity documents created.".format(type_of_identity_document))
    return type_of_identity_document

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    types_of_identity_document_data = [
        {"code":"CC", "description":"Citizenship Card"},
        {"code":"CE", "description":"Foreign ID Card"},
        {"code":"NIP", "description":"Number of personal identification"},
        {"code":"NIT", "description":"Tax identification number"},
        {"code":"TI", "description":"Identity Card"},
        {"code":"PAP", "description":"Passport"},
    ]

    # Creating types of identity document
    for data in types_of_identity_document_data:
        create_type_of_identity_document(data["code"], data["description"])