from django.urls import path
from .views import views, positionViews

urlpatterns = [
    path('', views.warehouseMain, name='warehouseMain'),
    path('<int:mainCategoryId>/<int:categoryId>/', positionViews.showPositions, name='showPositions'),
    path('<int:mainCategoryId>/<int:categoryId>/<int:positionId>/', positionViews.showPosition, name='showPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/', positionViews.addPosition, name='addPosition'),

    path('addMainCategory/', views.addMainCategory, name='addMainCategory'),
    path('<int:mainCategoryId>/addSubCategory/', views.addSubCategory, name='addSubCategory'),
]