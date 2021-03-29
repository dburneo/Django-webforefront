# from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_id>/', views.index, name="index_withid"),
    # path(r'^(?P<store_id>\d+)/$',views.index,name="index_withid"),
    path('contact/', views.ContactPage.as_view(), name="contact"),
    path('contact/<int:store_id>/', views.ContactPage.as_view(), name="contact_with_id"),
]