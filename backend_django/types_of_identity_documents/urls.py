from django.urls import include, path
from . import views

urlpatterns = [
    path('api/types_of_identity_documents', views.RetrieveTypesOfIdentityDocumentsView.as_view(), name='retrieve-types_of_identity_documentsview'),
]