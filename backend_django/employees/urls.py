from django.urls import include, path
from . import views

urlpatterns = [
    path('api/employees', views.RetrieveEmployeesView.as_view(), name='retrieve-employeesview'),
    path('api/save-employees', views.CreateEmployeesView.as_view(), name='save-employeesview'),
]