from rest_framework import serializers

from .models import Data


class DataSerializer(serializers.ModelSerializer):
    d = serializers.DateTimeField(source='date', format="%Y-%m-%d %H:%M:%S")
    v = serializers.FloatField(source='value')

    class Meta:
        model = Data
        fields = ('id', 'd', 'v')
