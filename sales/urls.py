from django.urls import path
from .views import SalesList, SaleDetail, SaleDelete, SaleCreate, SaleUpdate

urlpatterns = [
    path('', SalesList.as_view(), name='salesList'),
    path('create/', SaleCreate.as_view(), name='saleCreate'),
    path('<slug:name>/', SaleDetail.as_view(), name='saleDetail'),
    path('<slug:name>/delete/', SaleDelete.as_view(), name='saleDelete')
]