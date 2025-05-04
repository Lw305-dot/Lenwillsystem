from rest_framework import serializers
from .models import Asset, TechnicalData, WorkOrder, MaintenanceLog

class TechnicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalData
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    technical_data = TechnicalDataSerializer(many=True, read_only=True)

    class Meta:
        model = Asset
        fields = '__all__'

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'

class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = '__all__'
