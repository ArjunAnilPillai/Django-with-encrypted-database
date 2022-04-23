from django.urls import path
from .views import *

urlpatterns = [
    path("", submitPage, name="submitPage"),
    path("display/", displayPage, name="displayPage"),
]
