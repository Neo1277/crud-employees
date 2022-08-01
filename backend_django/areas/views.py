from rest_framework import generics

from .models import Areas

from .serializers import AreasSerializer

class RetrieveAreasView(generics.ListAPIView):
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer