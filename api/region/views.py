from django.shortcuts import render

# Create your views here.

from .models import Region
from rest_framework import viewsets, permissions
from .serializers import RegionSerializer

class RegionViewSetList(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAdminUser]