from django.urls import path
from .views import views, positionViews

urlpatterns = [
     

    path('', views.warehouseMain, name='warehouseMain'),
    #path('show/', CategoryValuesList.as_view(), name="show"),
    #path('<int:mainCategoryId>/<int:categoryId>/', positionViews.showPositions, name='showPositions'),
    path('<mainCategoryId>/<categoryId>/', positionViews.PositionsList.as_view(), name='showPositions'),
    #path('<int:mainCategoryId>/<int:categoryId>/<int:positionId>/', positionViews.showPosition, name='showPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/', positionViews.PositionDetailView.as_view(), name='showPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/', positionViews.addPosition, name='addPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/execute/', positionViews.addPositionExecute, name='addPositionExecute'),
    #path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/', positionViews.showCategoryValues, name='showCategoryValues'),
    path('<mainCategoryId>/<categoryId>/showCategoryValues/', positionViews.CategoryValuesList.as_view(), name='showCategoryValues'),

    path('addMainCategory/', views.addMainCategory, name='addMainCategory'),
    path('<int:mainCategoryId>/addSubCategory/', views.addSubCategory, name='addSubCategory'),
]