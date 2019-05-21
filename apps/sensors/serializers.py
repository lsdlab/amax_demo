from rest_framework import serializers
from .models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = ('id', 'temp', 'collected_at', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
