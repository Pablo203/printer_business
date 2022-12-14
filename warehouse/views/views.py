from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ..models import MainCategory, Category, Position, CategoryValue
from ..forms import addCategoryForm
from django.views.generic import ListView
import logging
_logger = logging.getLogger('django')
# Create your views here.

def warehouseMain(request):
    return render(request, 'warehouseMain.html', {})

def addMainCategory(request):
    if request.method == "POST":
        form = addCategoryForm(request.POST)
        if form.is_valid():
            mainCategory = MainCategory(
                name = form.cleaned_data['name'],
            )
            mainCategory.save()
    
    return HttpResponseRedirect(reverse('warehouseMain'))

def addSubCategory(request, mainCategoryId):
    if request.method == "POST":
        form = addCategoryForm(request.POST)
        mainCategory = MainCategory.objects.get(id=mainCategoryId)
        if form.is_valid():
            category = Category(
                name = form.cleaned_data['name'],
                topCategory = mainCategory
            )
            category.save()
    
    return HttpResponseRedirect(reverse('warehouseMain'))

class CategoryValuesList(ListView):
    model = CategoryValue
    template_name = 'categoryvalue_list.html'

    context_object_name = "categoryValues"

    def get_queryset(self):
        return CategoryValue.objects.filter(category=self.kwargs['categoryId'])

def showCategoryDeleteView(request, mainCategoryId, categoryId, propertyName):
    category = Category.objects.get(id=categoryId)
    return render(request, 'confirmCategoryValueDelete.html', {'propertyName': propertyName, 'category': category})

def showCategoryDeleteExecute(request, mainCategoryId, categoryId, propertyName):
    positions = Position.objects.filter(category=Category.objects.get(id=categoryId))
    positionsData = []
    for position in positions:
        if propertyName in position.data:
            position.data.pop(propertyName)
            position.save()
        positionsData.append(position.data)
    categoryValue = CategoryValue.objects.filter(propertyName=propertyName)
    if categoryValue.count():
        categoryValue.delete()
    return HttpResponseRedirect(reverse('showCategoryValues', kwargs={'mainCategoryId': mainCategoryId ,'categoryId': categoryId}))
    
def showCategoryCreateView(request, mainCategoryId, categoryId):
    return render(request, 'categoryValueCreate.html', {'mainCategoryId': mainCategoryId ,'categoryId': categoryId})


def showCategoryCreateExecute(request, mainCategoryId, categoryId):
    if request.method == "POST":
        form = addCategoryForm(request.POST)
        if form.is_valid():
            category_value = CategoryValue(
                propertyName = form.cleaned_data['name'],
                category = Category.objects.get(id=categoryId)
            )
            category_value.save()
            positions = Position.objects.filter(category=categoryId)
            for position in positions:
                position.data[form.cleaned_data['name']] = ""
                position.save()
    return HttpResponseRedirect(reverse('showCategoryValues', kwargs={'mainCategoryId': mainCategoryId ,'categoryId': categoryId}))


def deleteCategory(request, mainCategoryId, categoryId):
    return HttpResponse("CHECK")

def deleteCategoryExecute(request, mainCategoryId, categoryId):
    pass