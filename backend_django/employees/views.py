from rest_framework import generics, pagination

from .models import Employees

from .serializers import EmployeesSerializer

# Open Django console
# python manage.py shell

# pagination: https://www.django-rest-framework.org/api-guide/pagination/
class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

class RetrieveEmployeesView(generics.ListAPIView):
    queryset = Employees.objects.get_all()
    serializer_class = EmployeesSerializer
    pagination_class = LargeResultsSetPagination
