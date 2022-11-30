from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ..models import MainCategory, Category, Position
from ..forms import addCategoryForm
# Create your views here.

def showPositions(request, mainCategoryId, categoryId):
    positions = Position.objects.filter(category=categoryId)
    return render(request, 'warehouseElements.html', {'positions': positions})

def showPosition(request, mainCategoryId, categoryId, positionId):
    position = Position.objects.get(id=positionId)
    return render(request, 'warehousePosition.html',
    {'position': position})

def addPosition(request):
    pass
