from rest_framework import serializers

from .models import Employees, ThirdParties

from django_countries.serializer_fields import CountryField

from rest_framework.validators import UniqueTogetherValidator

from dateutil.relativedelta import relativedelta

from datetime import datetime

class RetrieveEmployeesSerializer(serializers.ModelSerializer):
    # DRF custom serializer:
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

class SaveEmployeesSerializer(serializers.ModelSerializer):

    country = CountryField()

    date_of_entry = serializers.DateTimeField(required=True)

    area_id = serializers.CharField(required=True)

    def validate_date_of_entry(self, value):
        """
        Check that the date of entry is after or equal one month before
        the current date and before or equal the current date.
        """
        date_of_entry = str(value)
        date_of_entry = date_of_entry[:19]
        date_of_entry = datetime.strptime(date_of_entry, '%Y-%m-%d %H:%M:%S')

        current_date = datetime.now()

        previous_date = datetime.now() - relativedelta(months=1)

        if date_of_entry < previous_date:
            raise serializers.ValidationError("The date must be after or equal "+ str(previous_date))

        if date_of_entry > current_date:
            raise serializers.ValidationError("The date must be before or equal "+ str(current_date))

        return value

    class Meta:
        model = Employees
        fields = ['country',
                  'area_id',
                  'date_of_entry']

class SaveThirdPartiesSerializer(serializers.ModelSerializer):

    identity_document = serializers.RegexField(regex='^(\w+\d+|\d+\w+)+$',
                                        required=True, max_length=20)

    last_name = serializers.RegexField(regex='^[A-Z]+$',
                                        required=True, max_length=20)

    second_surname = serializers.RegexField(regex='^[A-Z]+$',
                                        required=True, max_length=20)

    first_name = serializers.RegexField(regex='^[A-Z]+$',
                                        required=True, max_length=20)

    middle_names = serializers.RegexField(regex='^[A-Z ]+$',
                                          required=False, max_length=50,
                                          allow_blank=True)

    email =  serializers.EmailField(max_length=300)

    types_of_identity_documents_id = serializers.CharField(required=True)

    third_parties_employees = SaveEmployeesSerializer()

    def validate_if_identity_document_and_type_exist(self,
                                                     identity_document,
                                                     types_of_identity_documents_id):
        """
        Check that there isn't an identity document with the same
        type registered yet.
        """
        validate_identity_document = ThirdParties.objects.filter(
            identity_document=identity_document,
            types_of_identity_documents_id=types_of_identity_documents_id
        )

        return validate_identity_document

    def validate(self, data):

        if self.validate_if_identity_document_and_type_exist(
                data['identity_document'],
                data['types_of_identity_documents_id']
        ):
            raise serializers.ValidationError("There is already an employee with the same "
                                              "identity document and type of identity "
                                              "document")

        return data

    # write nested serialization:
    # https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
    def create(self, validated_data):

        employee_data = validated_data.pop('third_parties_employees')

        third_party = ThirdParties.objects.create(**validated_data)

        Employees.objects.create(third_party=third_party, **employee_data)

        return third_party

    class Meta:
        model = ThirdParties
        fields = ['identity_document',
                  'types_of_identity_documents_id',
                  'last_name',
                  'second_surname',
                  'first_name',
                  'middle_names',
                  'email',
                  'third_parties_employees']
