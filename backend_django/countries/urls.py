from django.urls import include, path
from . import views

urlpatterns = [
    path('api/countries', views.RetrieveCountriesView.as_view(), name='retrieve-countriesview'),
]