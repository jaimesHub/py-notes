from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def greeting(request):
    return HttpResponse("Hello, world")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
