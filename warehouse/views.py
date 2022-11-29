from django.shortcuts import render
from django.http import HttpResponse
from .models import MainCategory, Category
# Create your views here.

def warehouseMain(request):
    mainCategories = MainCategory.objects.all()
    categories = Category.objects.all()
    return render(request, 'warehouseMain.html', {'mainCategories': mainCategories, 'categories': categories})



def addPosition(request):
    pass

def addCategory(request):
    pass

def addCategoryItem(request):
    pass