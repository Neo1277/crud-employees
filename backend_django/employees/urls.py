from django.urls import include, path
from . import views

urlpatterns = [
    path('api/employees', views.RetrieveEmployeesView.as_view(), name='retrieve-employeesview'),
    path('api/save-employees', views.CreateEmployeesView.as_view(), name='save-employeesview'),
    path('api/update-employees/<int:pk>', views.UpdateEmployeesView.as_view(), name='update-employeesview'),
    path('api/delete-employees/<int:pk>', views.DeleteEmployeesView.as_view(), name='delete-employeesview'),

    path('api/retrieve-new-email/<str:last_name>/<str:first_name>/<str:country_code>',
         views.RetrieveNewEmailView.as_view(), name='retrieve-new-email-employeesview'),
    path('api/retrieve-new-email/<str:last_name>/<str:first_name>/<str:country_code>'
         '/<int:pk>', views.RetrieveNewEmailView.as_view(), name='retrieve-new-email-employeesview'),
]