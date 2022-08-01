from django.urls import include, path
from . import views

urlpatterns = [
    path('api/areas', views.RetrieveAreasView.as_view(), name='retrieve-areasview'),
]