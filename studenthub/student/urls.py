from django.urls import path
from . import views


urlpatterns = [
    path("", views.temp_view, name="temp_view"),
]
