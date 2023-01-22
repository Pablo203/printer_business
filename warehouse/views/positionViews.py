import logging
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from contacts.models import Contact

from ..forms import UploadFileForm, addCategoryForm, addCategoryValueForm
from ..models import Category, CategoryValue, MainCategory, Position, Vendor

_logger = logging.getLogger('django')
# Create your views here.


class PositionDetailView(DetailView):
    model = Position
    template_name = "position_detail.html"
    context_object_name = "position"

    def get_queryset(self):
        return Position.objects.filter(id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position = Position.objects.get(id=self.kwargs["pk"])
        context['vendors'] = Vendor.objects.filter(product=position)
        return context


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
        data_holder = {}
        skipKeys = ['csrfmiddlewaretoken', 'name', 'amount', 'imgInput']
        for key, value in data.items():
            if key not in skipKeys:
                data_holder[key] = value

        position = Position(
            name = data['name'],
            category = Category.objects.get(id=categoryId),
            data = data_holder
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
        position = Position.objects.get(id=self.kwargs["pk"])
        context['vendors'] = Vendor.objects.filter(product=position)
        vendor_array = []
        for vendor in context['vendors']:
            vendor_array.append(vendor.vendor)
        free_vendors = []
        for contact in Contact.objects.all():
            if contact not in vendor_array:
                free_vendors.append(contact)
        context['allVendors'] = free_vendors 
        context['categoryValues'] = CategoryValue.objects.filter(category=Category.objects.get(id=self.kwargs['categoryId']))
        context['position'] = Position.objects.get(id=self.kwargs['pk'])
        return context

def editPositionExecute(request, mainCategoryId, categoryId, pk):
    if request.method == "POST":
        data = request.POST
        position = Position.objects.get(id=pk)

        dataHolder = {}
        vendorsHolder = []
        
        skipKeys = ['csrfmiddlewaretoken', 'name', 'amount']
        for key, value in data.items():
            if key not in skipKeys and "vendor" not in key:
                dataHolder[key] = value
            if "vendor" in key:
                vendorsHolder.append(value)

        for i in range(0,len(vendorsHolder),2):
            try:
                vendor = Vendor.objects.get(product=Position.objects.get(name=position.name), vendor=Contact.objects.get(name=vendorsHolder[i]))
                vendor.price = vendorsHolder[i+1]
                vendor.save()
            except:
                if float(vendorsHolder[i+1]) > 0:
                    newVendor = Vendor(
                        vendor = Contact.objects.get(name=vendorsHolder[i]),
                        product = Position.objects.get(name=position.name),
                        price = vendorsHolder[i+1]
                    )
                    newVendor.save()

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

def deleteVendor(request, mainCategoryId, categoryId, pk, vendor, price):
    position = Position.objects.get(id=pk)

    vendors = Vendor.objects.filter(product=position, vendor=Contact.objects.get(name=vendor), price=float(price))
    vendors.delete()

    return redirect('showPosition', mainCategoryId=mainCategoryId ,categoryId=categoryId, pk=pk)