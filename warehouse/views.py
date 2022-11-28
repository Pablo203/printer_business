from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def warehouseMain(request):
    return render(request, 'warehouseMain.html', {})