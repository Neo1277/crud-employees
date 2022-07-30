from django.db import models

from areas.models import UnsignedAutoField
from types_of_identity_documents.models import TypesOfIdentityDocuments
from django_countries.fields import CountryField
from areas.models import Areas

class ThirdParties(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    identity_document = models.CharField(max_length=20)

    types_of_identity_documents = models.ForeignKey(
        TypesOfIdentityDocuments,
        on_delete=models.CASCADE,
        related_name='types_of_identity_documents_third_parties'
    )

    last_name = models.CharField(max_length=20)

    second_surname = models.CharField(max_length=20)

    first_name = models.CharField(max_length=20)

    middle_names = models.CharField(max_length=50, null=True)

    email = models.EmailField(max_length=300, unique=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

class Employees(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    third_party = models.ForeignKey(
        ThirdParties,
        on_delete=models.CASCADE,
        related_name='third_parties_employees'
    )

    country = CountryField()

    area = models.ForeignKey(
        Areas,
        on_delete=models.CASCADE,
        related_name='areas_employees'
    )

    date_of_entry = models.DateTimeField()

    INACTIVE = '0'
    ACTIVE = '1'
    STATUS_CHOICES = [
        (INACTIVE, 'Active'),
        (ACTIVE, 'Inactive'),
    ]

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )