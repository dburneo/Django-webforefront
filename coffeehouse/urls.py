"""coffeehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings

from django.contrib import admin
from django.urls import path, re_path, register_converter, include
from django.views.generic import TemplateView

from coffeehouse.utils import converters

register_converter(converters.RomanNumeralConverter, 'roman')
register_converter(converters.FloatConverter, 'float')

from coffeehouse.about import views as about_views
from coffeehouse.stores import views as stores_views

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('about/', include('coffeehouse.about.urls')),
    path('banners/', include('coffeehouse.banners.urls')),
    path('stores/', include('coffeehouse.stores.urls')),
    path('admin/', admin.site.urls),
    path('<roman:year>/', TemplateView.as_view(template_name='homepage.html')),
    path('<float:float_number>/', TemplateView.as_view(template_name='homepage.html')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('', TemplateView.as_view(template_name='homepage.html')),
    path('drinks/<str:drink_name>/', TemplateView.as_view(template_name='drinks/index.html')),
]
