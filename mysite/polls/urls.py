from django.urls import path

from . import views

urlpatterns = [
    path('8888', views.index, name='index'),
]

