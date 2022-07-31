# https://stackoverflow.com/a/51577650
# backend_django/areas/management/commands/seed_areas.py
# python manage.py seed_areas
from django.core.management.base import BaseCommand

from areas.models import Areas

import logging
logger = logging.getLogger(__name__)

# python manage.py seed --mode=refresh

""" Clear all data and creates areas """
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
    logger.info("Delete Areas instances")
    Areas.objects.all().delete()

def create_area(value: str):
    """Creates an area object with elements from the list"""

    area = Areas(
        description=value,
    )
    area.save()
    logger.info("{} area created.".format(area))
    return area

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    area_data = [
        "Administration",
        "Financial",
        "Shopping",
        "Infraestructure",
        "Operations",
        "Human Resources",
        "Various Services"
    ]

    # Creating areas
    for value in area_data:
        create_area(value)