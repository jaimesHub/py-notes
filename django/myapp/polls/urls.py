from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hi/", views.greeting, name="greeting"),
]