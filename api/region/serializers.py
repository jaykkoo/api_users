from rest_framework import serializers
from .models import Region

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['region']