from django.urls import path 

from . import views


app_name = "api"

urlpatterns = [
    path("detect", views.detect, name="detect")
]
