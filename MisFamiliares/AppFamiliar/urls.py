from django.urls import path
from AppFamiliar.views import *

urlpatterns = [
    path("familia/", familia, name="familia"),
    path("plantilla/", plantilla, name="plantilla"),
]