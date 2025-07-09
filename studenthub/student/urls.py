from django.urls import path
from . import views


urlpatterns = [
    path("", views.temp_form, name="temp_form"),
    path("main_page", views.main_page, name="main_page"),
    path("temp_cookies", views.temp_cookies, name="temp_cookies"),
    # authentication
    path("register", views.register, name="login"),
    path("login_view", views.login_view, name="login_view"),
    path("logout_view", views.logout_view, name="logout_view"),
]
