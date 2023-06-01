from rest_framework import serializers

from .models import Data


class DataSerializer(serializers.ModelSerializer):
    d = serializers.DateTimeField(source='date', format="%Y-%m-%d %H:%M:%S")
    v = serializers.FloatField(source='value')

    class Meta:
        model = Data
        fields = ('id', 'capteur', 'd', 'v')


class DataAddSerializer(serializers.Serializer):
    capteur = serializers.CharField(max_length=200)
    data = serializers.ListField(child=serializers.DictField())



# class DataSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     capteur = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     date = serializers.DateTimeField()
#     value = serializers.FloatField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Data` instance, given the validated data.
#         """
#         return Data.objects.create(**validated_data)
#   def update(self, instance, validated_data):
#         """
#         Update and return an existing `Data` instance, given the validated data.
#         """
#         instance.capteur = validated_data.get('capteur', instance.capteur)
#         instance.date = validated_data.get('date', instance.date)
#         instance.value = validated_data.get('value', instance.value)
#         instance.save()
#         return instance
