from rest_framework import generics

from .serializers import CountriesSerializer

from django_countries import countries

class RetrieveCountriesView(generics.ListAPIView):
    queryset = countries
    serializer_class = CountriesSerializer

