from django.db import models

from areas.models import UnsignedAutoField
from types_of_identity_documents.models import TypesOfIdentityDocuments
from django_countries.fields import CountryField
from areas.models import Areas

from django.db.models import F, Q

# Managers: https://docs.djangoproject.com/en/4.0/topics/db/managers/#creating-a-manager-with-queryset-methods
class ThirdPartiesManager(models.Manager):
    def validate_if_identity_document_and_type_exist(self,
                                                     identity_document,
                                                     types_of_identity_documents_id):
        return self.filter(
            identity_document=identity_document,
            types_of_identity_documents_id=types_of_identity_documents_id
        )

    def validate_if_email_exist(self,
                                last_name,
                                first_name):
        return self.values(
            'email'
        ).filter(
            last_name=last_name,
            first_name=first_name
        )

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

    objects = ThirdPartiesManager()

# Managers: https://docs.djangoproject.com/en/4.0/topics/db/managers/#creating-a-manager-with-queryset-methods
class EmployeesManager(models.Manager):
    def get_all(self):
        return self.values(
            'third_party__identity_document',
            'third_party__id',
            'third_party__last_name',
            'third_party__second_surname',
            'third_party__first_name',
            'third_party__middle_names',
            'third_party__email',
            'third_party__types_of_identity_documents__description',
            'third_party__types_of_identity_documents__id',
            'country',
            'area__id',
            'area__description',
            'id',
            'status',
            'date_of_entry',
            'created_at',
            'updated_at',
        ).annotate(
            identity_document=F('third_party__identity_document'),
            third_party_id=F('third_party__id'),
            last_name=F('third_party__last_name'),
            second_surname=F('third_party__second_surname'),
            first_name=F('third_party__first_name'),
            middle_names=F('third_party__middle_names'),
            email=F('third_party__email'),
            type_of_identity_document=F('third_party__types_of_identity_documents__description'),
            type_of_identity_document_id=F('third_party__types_of_identity_documents__id'),
            area_id=F('area__id'),
            area_description=F('area__description'),
            employee_id=F('id'),
        )

class Employees(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    third_party = models.OneToOneField(
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

    objects = EmployeesManager()

    class Meta:
        ordering = ['-id']