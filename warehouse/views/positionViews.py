from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from ..models import MainCategory, Category, Position, CategoryValue
from ..forms import addCategoryForm
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

    context_object_name = "categories"

    def get_queryset(self):
        return CategoryValue.objects.filter(category=self.kwargs['categoryId'])