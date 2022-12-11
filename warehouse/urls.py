from django.urls import path
from .views import views, positionViews

urlpatterns = [
     

    path('', views.warehouseMain, name='warehouseMain'),
    path('addMainCategory/', views.addMainCategory, name='addMainCategory'),
    path('<int:mainCategoryId>/addSubCategory/', views.addSubCategory, name='addSubCategory'),
    
    path('<int:mainCategoryId>/<int:categoryId>/', positionViews.PositionsList.as_view(), name='showPositions'),
 
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/', positionViews.addPosition, name='addPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/execute/', positionViews.addPositionExecute, name='addPositionExecute'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/', positionViews.CategoryValuesList.as_view(), name='showCategoryValues'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/create', positionViews.showCategoryCreateView, name='categoryValueCreate'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/confirmCreate', positionViews.showCategoryCreateExecute, name='categoryValueCreateConfirm'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/<str:propertyName>/delete', positionViews.showCategoryDeleteView, name='categoryValueDelete'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/<str:propertyName>/confirmDelete', positionViews.showCategoryDeleteExecute, name='categoryValueDeleteConfirm'),

    

    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/', positionViews.PositionDetailView.as_view(), name='showPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/editPosition/', positionViews.editPosition, name='editPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/editPositionExecute/', positionViews.editPositionExecute, name='editPositionExecute'),
]