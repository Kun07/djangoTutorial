from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^', views.home, name='blog-home'),
    url(r'^about/', views.about, name='blog-about'),
]