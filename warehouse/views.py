from django.shortcuts import render
from django.http import HttpResponse
from .models import MainCategory, Category, Position
# Create your views here.

def warehouseMain(request):
    return render(request, 'warehouseMain.html', {})

def showPositions(request, categoryId):
    positions = Position.objects.filter(category=categoryId)
    return render(request, 'warehouseElements.html', {'positions': positions})

def addPosition(request):
    pass

def addCategory(request):
    pass

def addCategoryItem(request):
    pass