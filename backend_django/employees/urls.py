from django.urls import include, path
from . import views

urlpatterns = [
    path('api/employees', views.RetrieveEmployeesView.as_view(), name='retrieve-employeesview'),
]