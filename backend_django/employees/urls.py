from django.urls import include, path
from . import views

urlpatterns = [
    path('api/employees', views.RetrieveEmployeesView.as_view(), name='retrieve-employeesview'),
    path('api/save-employees', views.CreateEmployeesView.as_view(), name='save-employeesview'),
    path('api/update-employees/<int:pk>/', views.UpdateEmployeesView.as_view(), name='update-employeesview'),
]