
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets

from .models import Data
from .serializers import DataSerializer


def list_datas(request):
    datas = Data.objects.all()
    return render(request, 'gazapp/listdatas.html', {"datas": datas})


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

