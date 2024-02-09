from django.urls import path
# from django_project.blog import views -> ModuleNotFoundError: No module named 'django_project.blog' 
from . import views

urlpatterns = [
    path("", views.home, name="posts"), # define a route that maps the blog URL
    path("about/", views.about, name="about")
]