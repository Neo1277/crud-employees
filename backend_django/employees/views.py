from rest_framework import generics, pagination

from .models import Employees, ThirdParties

from .serializers import (
    RetrieveEmployeesSerializer,
    SaveThirdPartiesSerializer,
    UpdateThirdPartiesSerializer
)

from django.http.response import JsonResponse

from rest_framework.views import APIView

from .email_generation import check_email

from rest_framework import filters

# Open Django console
# python manage.py shell

# pagination: https://www.django-rest-framework.org/api-guide/pagination/
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

# https://stackoverflow.com/a/58375919
# https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
class RetrieveEmployeesView(generics.ListAPIView):
    queryset = Employees.objects.get_all().order_by('-id')
    serializer_class = RetrieveEmployeesSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'third_party__identity_document',
        'third_party__types_of_identity_documents__description',
        'third_party__last_name',
        'third_party__second_surname',
        'third_party__first_name',
        'third_party__middle_names',
        'country',
        'third_party__email',
        'area__description',
    ]

# Generic views:
# https://www.django-rest-framework.org/api-guide/generic-views/
class CreateEmployeesView(generics.CreateAPIView):
    serializer_class = SaveThirdPartiesSerializer

class UpdateEmployeesView(generics.UpdateAPIView):
    queryset = ThirdParties.objects.all()
    serializer_class = UpdateThirdPartiesSerializer

class DeleteEmployeesView(generics.DestroyAPIView):
    queryset = ThirdParties.objects.all()

class RetrieveNewEmailView(APIView):

    def get(self, request, last_name, first_name, country_code, pk=None):
        """
        Return email generated automatically according to the parameters
        """
        email = check_email(last_name, first_name, country_code, pk)
        data = {
            "email": email
        }
        return JsonResponse(data, safe=False)