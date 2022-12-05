from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ..models import MainCategory, Category, Position, CategoryValue
from ..forms import addCategoryForm
# Create your views here.

def showPositions(request, mainCategoryId, categoryId):
    positions = Position.objects.filter(category=categoryId)
    return render(request, 'warehouseElements.html', {'positions': positions, 'mainCategoryId': mainCategoryId, 'categoryId': categoryId})

def showPosition(request, mainCategoryId, categoryId, positionId):
    position = Position.objects.get(id=positionId)
    return render(request, 'warehousePosition.html',
    {'position': position})

def addPosition(request, mainCategoryId, categoryId):
    categoryValues = CategoryValue.objects.filter(category=categoryId)
    return render(request, 'warehouseAddPosition.html', {'categoryValues': categoryValues, 'mainCategoryId': mainCategoryId, 'categoryId': categoryId})

def addPositionExecute(request, mainCategoryId, categoryId):
    if request.method == "POST":
        data = request.POST
        dataHolder = {}
        for key, value in data.items():
            if key != 'csrfmiddlewaretoken' and key != 'name':
                dataHolder[key] = value

        position = Position(
            name = data['name'],
            category = Category.objects.get(id=categoryId),
            data = dataHolder
        )
        position.save()
    return HttpResponseRedirect(reverse('showPositions', kwargs={'mainCategoryId': mainCategoryId ,'categoryId': categoryId}))

def showCategoryValues(request, mainCategoryId, categoryId):
    properties = CategoryValue.objects.filter(category=categoryId)
    return HttpResponse(properties)