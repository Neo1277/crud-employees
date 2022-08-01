from rest_framework import generics

from .models import TypesOfIdentityDocuments

from .serializers import TypesOfIdentityDocumentsSerializer

class RetrieveTypesOfIdentityDocumentsView(generics.ListAPIView):
    queryset = TypesOfIdentityDocuments.objects.all()
    serializer_class = TypesOfIdentityDocumentsSerializer