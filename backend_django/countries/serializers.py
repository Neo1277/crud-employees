from rest_framework import serializers

class CountriesSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()