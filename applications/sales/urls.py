from django.urls import path

from . import views

from .view import UserRegister, UsersCSV

urlpatterns = [
    path("", views.index, name="index"),
    path("users", UserRegister.as_view(), name="users"),
    path("users_csv", UsersCSV.as_view(), name="users_csv"),
]
