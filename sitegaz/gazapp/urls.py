from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"datas", views.DataViewSet, basename="datas")

urlpatterns = [
    path("", views.list_datas, name="listdatas"),
    path("api/", include(router.urls)),
]

