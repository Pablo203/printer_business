from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ..models import MainCategory, Category, Position
from ..forms import addCategoryForm
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