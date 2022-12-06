from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ..models import MainCategory, Category, Position, CategoryValue
from ..forms import addCategoryForm, UploadFileForm
from django.views.generic import ListView, DetailView
# Create your views here.


class PositionDetailView(DetailView):
    model = Position
    template_name = "position_detail.html"
    context_object_name = "position"

    def get_queryset(self):
        return Position.objects.filter(id=self.kwargs["pk"])

def addPosition(request, mainCategoryId, categoryId):
    categoryValues = CategoryValue.objects.filter(category=categoryId)
    return render(request, 'warehouseAddPosition.html', {'categoryValues': categoryValues, 'mainCategoryId': mainCategoryId, 'categoryId': categoryId})

def handle_uploaded_file(request, f, positionId):
    name = f.name
    position = Position.objects.get(id=positionId)
    
    with open('/home/a4ch3r/Documents/printer_business/static/positionImgs/%s' % name, 'ab') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    position.imagePath = '/static/positionImgs/%s' % name
    position.save()

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
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        handle_uploaded_file(request, request.FILES['imgInput'], position.id)
    #return HttpResponse(request.FILES)
    return HttpResponseRedirect(reverse('showPositions', kwargs={'mainCategoryId': mainCategoryId ,'categoryId': categoryId}))

class PositionsList(ListView):
    model = Position
    template_name = "position_list.html"

    context_object_name = "positions"

    def get_queryset(self):
        return Position.objects.filter(category=self.kwargs['categoryId'])

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['mainCategoryId'] = self.kwargs['mainCategoryId']
        context['categoryId'] = self.kwargs['categoryId']
        return context

class CategoryValuesList(ListView):
    model = CategoryValue
    template_name = 'categoryvalue_list.html'

    context_object_name = "categoryValues"

    def get_queryset(self):
        return CategoryValue.objects.filter(category=self.kwargs['categoryId'])