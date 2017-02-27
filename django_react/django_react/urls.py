"""django_react URL Configuration"""
from django.conf.urls import url
from django.contrib import admin
from react import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
