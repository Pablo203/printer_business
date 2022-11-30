from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouseMain, name='warehouseMain'),
    path('<int:mainCategoryId>/<int:categoryId>/', views.showPositions, name='showPositions'),

    path('addMainCategory/', views.addMainCategory, name='addMainCategory'),
    path('<int:mainCategoryId>/addSubCategory/', views.addSubCategory, name='addSubCategory'),
]