from rest_framework import generics, permissions, views
from core import models, utils
from core.api.location.serializers import LocationSerializer
from rest_framework import response, status, parsers
from collections import OrderedDict

class CreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = models.Location.objects.all()
    serializer_class = LocationSerializer
