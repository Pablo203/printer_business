from django.urls import path
from .views import SalesList, SaleDetail

urlpatterns = [
    path('', SalesList.as_view(), name='salesList'),
    path('<slug:name>/', SaleDetail.as_view(), name='saleDetail'),
]