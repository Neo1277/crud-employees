from rest_framework import serializers

from .models import TypesOfIdentityDocuments

class TypesOfIdentityDocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypesOfIdentityDocuments
        fields = ('__all__')