from rest_framework import generics

from .models import Employees

from .serializers import EmployeesSerializer

# Open Django console
# python manage.py shell

class RetrieveEmployeesView(generics.ListAPIView):
    queryset = Employees.objects.get_all()
    serializer_class = EmployeesSerializer
