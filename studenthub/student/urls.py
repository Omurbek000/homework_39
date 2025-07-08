from django.urls import path
from . import views


urlpatterns = [
    path("", views.temp_form, name="temp_form"),
    path("main_page", views.main_page, name="main_page"),
]
