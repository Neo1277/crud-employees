from rest_framework import serializers

from .models import Employees, ThirdParties

from django_countries.serializer_fields import CountryField

from rest_framework.validators import UniqueValidator

from dateutil.relativedelta import relativedelta

from datetime import datetime

from django.db.models import Q

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
    date_of_entry = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    country = CountryField(country_dict=True)
    area_id = serializers.CharField(read_only=True)
    area_description = serializers.CharField(read_only=True)
    employee_id = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

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

    # validators:
    # https://www.django-rest-framework.org/api-guide/validators/#uniquevalidator
    email =  serializers.EmailField(max_length=300,
                                    validators=[
                                        UniqueValidator(
                                            queryset=ThirdParties.objects.all()
                                        )
                                    ]
    )

    types_of_identity_documents_id = serializers.CharField(required=True)

    third_parties_employees = SaveEmployeesSerializer()

    def validate(self, data):
        validate_if_identity_document_and_type_exist = ThirdParties.objects.validate_if_identity_document_and_type_exist(
            data['identity_document'],
            data['types_of_identity_documents_id']
        )

        if validate_if_identity_document_and_type_exist:
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

class UpdateThirdPartiesSerializer(SaveThirdPartiesSerializer):

    def validate(self, data):

        # Query unequals: https://stackoverflow.com/a/1154977
        validate_if_identity_document_and_type_exist = ThirdParties.objects.validate_if_identity_document_and_type_exist(
            data['identity_document'],
            data['types_of_identity_documents_id']
        ).filter(~Q(id=self.instance.id))

        if validate_if_identity_document_and_type_exist:
            raise serializers.ValidationError("There is already an employee with the same "
                                              "identity document and type of identity "
                                              "document")

        return data

    def update(self, instance, validated_data):

        employee_data = validated_data.pop('third_parties_employees')

        instance.identity_document = validated_data.get('identity_document', instance.identity_document)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.second_surname = validated_data.get('second_surname', instance.second_surname)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_names = validated_data.get('middle_names', instance.middle_names)
        instance.email = validated_data.get('email', instance.email)
        instance.types_of_identity_documents_id = validated_data.get('types_of_identity_documents_id', instance.types_of_identity_documents_id)
        instance.save()

        employee = Employees.objects.get(third_party=instance)  # this will crash if the id is invalid though
        employee.country = employee_data.get('country', employee.country)
        employee.date_of_entry = employee_data.get('date_of_entry', employee.date_of_entry)
        employee.area_id = employee_data.get('area_id', employee.area_id)
        employee.save()

        return instance
