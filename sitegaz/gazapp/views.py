
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Data
from .serializers import DataSerializer, DataAddSerializer


def list_datas(request):
    datas = Data.objects.all()
    return render(request, 'gazapp/listdatas.html', {"datas": datas})


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return DataAddSerializer
        return DataSerializer

    def create(self, request, *args, **kwargs):
        serializer = DataAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        capteur = serializer.validated_data['c']
        data_list = serializer.validated_data['d']

        instances = []

        for data in data_list:
            date = data['t']
            value = data['v']
            instance = Data.objects.create(capteur=capteur, date=date, value=value)
            instances.append(instance)
        return Response(DataSerializer(instances, many=True).data)
