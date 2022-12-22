from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ..models import MainCategory, Category, Position, CategoryValue
from ..forms import addCategoryForm, UploadFileForm, addCategoryValueForm
from django.views.generic import ListView, DetailView, TemplateView
import os
import logging
_logger = logging.getLogger('django')
# Create your views here.


class PositionDetailView(DetailView):
    model = Position
    template_name = "position_detail.html"
    context_object_name = "position"

    def get_queryset(self):
        return Position.objects.filter(id=self.kwargs["pk"])


class PositionAdd(TemplateView):
    template_name = 'warehouseAddPosition.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['categoryValues'] = CategoryValue.objects.filter(category=self.kwargs['categoryId'])
        return context

def handle_uploaded_file(request, f, positionId):
    name = f.name
    position = Position.objects.get(id=positionId)
    if os.path.isfile('/home/a4ch3r/Documents/printer_business/static/positionImgs/%s' % name):
        position.imagePath = '/static/positionImgs/%s' % name
        position.save()
    else:
        with open('/home/a4ch3r/Documents/printer_business/static/positionImgs/%s' % name, 'ab') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        position.imagePath = '/static/positionImgs/%s' % name
        position.save()

def addPositionExecute(request, mainCategoryId, categoryId):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        data = request.POST
        dataHolder = {}
        skipKeys = ['csrfmiddlewaretoken', 'name', 'amount', 'imgInput']
        for key, value in data.items():
            if key not in skipKeys:
                dataHolder[key] = value

        position = Position(
            name = data['name'],
            category = Category.objects.get(id=categoryId),
            data = dataHolder
        )
        position.save()
        
        if "imgInput" in request.FILES:
            handle_uploaded_file(request, request.FILES['imgInput'], position.id)
    return HttpResponseRedirect(reverse('showPositions', kwargs={'mainCategoryId': mainCategoryId ,'categoryId': categoryId}))

class PositionsList(ListView):
    model = Position
    template_name = "position_list.html"

    context_object_name = "positions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mainCategoryId'] = self.kwargs['mainCategoryId']
        context['categoryId'] = self.kwargs['categoryId']
        return context

    def get_queryset(self):
        return Position.objects.filter(category=self.kwargs['categoryId'])

class EditPosition(TemplateView):
    template_name = 'warehouseEditPosition.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['categoryValues'] = CategoryValue.objects.filter(category=Category.objects.get(id=self.kwargs['categoryId']))
        context['position'] = Position.objects.get(id=self.kwargs['pk'])
        return context

def editPositionExecute(request, mainCategoryId, categoryId, pk):
    if request.method == "POST":
        data = request.POST
        position = Position.objects.get(id=pk)

        dataHolder = {}
        skipKeys = ['csrfmiddlewaretoken', 'name', 'amount']
        for key, value in data.items():
            if key not in skipKeys:
                dataHolder[key] = value

        position.name = data['name']
        position.amount = data['amount']
        position.data = dataHolder
        position.save()
        if "imgInput" in request.FILES:
            handle_uploaded_file(request, request.FILES['imgInput'], position.id)
        

    return HttpResponseRedirect(reverse('showPosition', kwargs={'mainCategoryId': mainCategoryId ,'categoryId': categoryId, 'pk': pk}))

class DeletePosition(TemplateView):
    template_name = 'positionDelete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position'] = Position.objects.get(id=self.kwargs['pk'])
        return context

def deletePositionExecute(request, mainCategoryId, categoryId, pk):
    position = Position.objects.get(id=pk)
    position.delete()
    return HttpResponseRedirect(reverse('showPositions', kwargs={'mainCategoryId': mainCategoryId ,'categoryId': categoryId}))