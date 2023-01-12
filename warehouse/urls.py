from django.urls import path
from .views import views, positionViews

urlpatterns = [
     

    path('', views.WarehouseMain.as_view(), name='warehouseMain'),
    path('addMainCategory/', views.addMainCategory, name='addMainCategory'),
    path('<int:mainCategoryId>/addSubCategory/', views.addSubCategory, name='addSubCategory'),
    
    path('<int:mainCategoryId>/<int:categoryId>/', positionViews.PositionsList.as_view(), name='showPositions'),
 
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/', positionViews.PositionAdd.as_view(), name='addPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/addPosition/execute/', positionViews.addPositionExecute, name='addPositionExecute'),
    path('<int:mainCategoryId>/<int:categoryId>/deleteCategory/', views.CategoryDelete.as_view(), name='deleteCategory'),
    path('<int:mainCategoryId>/<int:categoryId>/deleteCategory/execute', views.deleteCategoryExecute, name='deleteCategoryExecute'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/', views.CategoryValuesList.as_view(), name='showCategoryValues'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/create', views.CategoryValuesCreate.as_view(), name='categoryValueCreate'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/confirmCreate', views.showCategoryCreateExecute, name='categoryValueCreateConfirm'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/<str:propertyName>/delete', views.CategoryValuesDelete.as_view(), name='categoryValueDelete'),
    path('<int:mainCategoryId>/<int:categoryId>/showCategoryValues/<str:propertyName>/confirmDelete', views.showCategoryDeleteExecute, name='categoryValueDeleteConfirm'),

    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/editPosition/', positionViews.EditPosition.as_view(), name='editPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/editPositionExecute/', positionViews.editPositionExecute, name='editPositionExecute'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/deletePosition/', positionViews.DeletePosition.as_view(), name='deletePosition'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/deletePositionExecute/', positionViews.deletePositionExecute, name='deletePositionExecute'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/', positionViews.PositionDetailView.as_view(), name='showPosition'),
    path('<int:mainCategoryId>/<int:categoryId>/<slug:pk>/<str:vendor>/<str:price>', positionViews.deleteVendor, name='removeVendor'),
]