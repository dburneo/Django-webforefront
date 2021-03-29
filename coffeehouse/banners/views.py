from django.shortcuts import render
from django.urls import resolve

def index(request):
    return render(request, 'banners/index.html')
