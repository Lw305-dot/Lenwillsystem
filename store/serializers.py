from rest_framework import serializers
from .models import SparePart, PartRequest

class SparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePart
        fields = '__all__'

class PartRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRequest
        fields = '__all__'