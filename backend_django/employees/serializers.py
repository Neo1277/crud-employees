from rest_framework import serializers

from .models import Employees

from django_countries.serializer_fields import CountryField

class EmployeesSerializer(serializers.ModelSerializer):
    # DRF custom serializer "Field name is not valid for model" solution:
    # https://stackoverflow.com/a/67476280
    identity_document = serializers.CharField(read_only=True)
    third_party_id = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    second_surname = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    middle_names = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    type_of_identity_document = serializers.CharField(read_only=True)
    type_of_identity_document_id = serializers.CharField(read_only=True)
    country = CountryField(country_dict=True)
    area_id = serializers.CharField(read_only=True)
    area_description = serializers.CharField(read_only=True)
    employee_id = serializers.CharField(read_only=True)

    class Meta:
        model = Employees
        fields = ['identity_document',
                  'third_party_id',
                  'last_name',
                  'second_surname',
                  'first_name',
                  'middle_names',
                  'email',
                  'type_of_identity_document',
                  'type_of_identity_document_id',
                  'country',
                  'area_id',
                  'area_description',
                  'employee_id',
                  'status',
                  'date_of_entry',
                  'created_at',
                  'updated_at']