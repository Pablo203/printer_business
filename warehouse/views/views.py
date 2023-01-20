import logging

from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from ..forms import addCategoryForm
from ..models import Category, CategoryValue, MainCategory, Position

_logger = logging.getLogger('django')
# Create your views here.
class WarehouseMain(TemplateView):
    template_name = 'warehouseMain.html'

def addMainCategory(request):
    if request.method == "POST":
        form = addCategoryForm(request.POST)
        if form.is_valid():
            mainCategory = MainCategory(
                name = form.cleaned_data['name'],
            )
            mainCategory.save()
            Category(
                name="hide",
                topCategory=mainCategory
            )
    
    return HttpResponseRedirect(reverse('warehouseMain'))

def addSubCategory(request, mainCategoryId):
    if request.method == "POST":
        form = addCategoryForm(request.POST)
        mainCategory = MainCategory.objects.get(id=mainCategoryId)
        if form.is_valid():
            try:
                category = Category(
                    name = form.cleaned_data['name'],
                    topCategory = mainCategory
                )
                category.save()
            except IntegrityError:
                messages.add_message(request, messages.ERROR, "Category with this name already exists")
    
    return HttpResponseRedirect(reverse('warehouseMain'))

class CategoryValuesList(ListView):
    model = CategoryValue
    template_name = 'categoryvalue_list.html'
    
    # def get_queryset(self):
    #     return CategoryValue.objects.filter(category=self.kwargs['categoryId'])
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mainCategoryId'] = self.kwargs['mainCategoryId']
        context['categoryId'] = self.kwargs['categoryId']
        context['categoryValues'] = CategoryValue.objects.filter(category=self.kwargs['categoryId'])
        return context


class CategoryValuesDelete(TemplateView):
    template_name = 'confirmCategoryValueDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['categoryId'])
        return context

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

class CategoryValuesCreate(TemplateView):
    template_name = 'categoryValueCreate.html'

def showCategoryCreateExecute(request, mainCategoryId, categoryId):
    if request.method == "POST":
        form = addCategoryForm(request.POST)
        if form.is_valid():
            if CategoryValue.objects.filter(propertyName=form.cleaned_data['name']).exists():
                messages.add_message(request, messages.ERROR, "Category field with this name already exists")
            else:
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

class CategoryDelete(TemplateView):
    template_name = 'categoryDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['categoryId'])
        return context

def deleteCategoryExecute(request, mainCategoryId, categoryId):
    category = Category.objects.get(id=categoryId)
    category.delete()

    return HttpResponseRedirect(reverse('warehouseMain'))