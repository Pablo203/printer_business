from django.urls import path
from .views import views, positionViews

urlpatterns = [
     

    path('', views.warehouseMain, name='warehouseMain'),
    path('addMainCategory/', views.addMainCategory, name='addMainCategory'),
    path('<int:mainCategoryId>/addSubCategory/', views.addSubCategory, name='addSubCategory'),
    
    path('<mainCategoryId>/<categoryId>/', positionViews.PositionsList.as_view(), name='showPositions'),
 
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/', positionViews.addPosition, name='addPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/execute/', positionViews.addPositionExecute, name='addPositionExecute'),
    path('<mainCategoryId>/<categoryId>/showCategoryValues/', positionViews.CategoryValuesList.as_view(), name='showCategoryValues'),

    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/', positionViews.PositionDetailView.as_view(), name='showPosition'),

]