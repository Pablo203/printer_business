from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale

# Create your views here.

class SalesList(ListView):
    model = Sale

    context_object_name = 'sales'

class SaleDetail(DetailView):
    model = Sale

    slug_field = 'name'
    slug_url_kwarg = 'name'

    context_object_name = 'sale'

    # def get_queryset(self):
    #     return Sale.objects.get(name=self.kwargs['name'])