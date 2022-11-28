from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouseMain, name='warehouseMain')
]