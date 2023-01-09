from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactsList.as_view(), name='contactsList'),
    path('create/', ContactCreate.as_view(), name='contactCreate'),
    path('create/execute', executeContactCreate, name='contactCreateExecute'),
    path('<slug:pk>/', ContactDetail.as_view(), name='contactDetail'),
    path('<slug:pk>/edit',ContactDetailEdit.as_view(), name='editContact'),
    path('<slug:pk>/edit/execute', contactEditExecute, name='contactEditExecute'),
    path('<slug:pk>/delete', ContactDelete.as_view(), name='contactDelete'),
    path('<slug:pk>/delete/execute', contactDeleteExecute, name='contactDeleteExecute'),
]