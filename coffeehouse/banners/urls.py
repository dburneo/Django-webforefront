# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'banners_adverts'

urlpatterns = [
    path('', views.index, name="index"),
]
