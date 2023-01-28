from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Sale, SaleProduct

# Create your views here.

class SalesList(ListView):
    model = Sale

    context_object_name = 'sales'

class SaleDetail(DetailView):
    model = Sale

    slug_field = 'name'
    slug_url_kwarg = 'name'

    context_object_name = 'sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = SaleProduct.objects.filter(sale_order=Sale.objects.get(name=self.kwargs['name']))

        return context

    # def get_queryset(self):
    #     return Sale.objects.get(name=self.kwargs['name'])

class SaleCreate(CreateView):
    model = Sale

    fields = ['client']

    template_name_suffix = '_create'

    success_url = reverse_lazy('salesList')

class SaleUpdate(UpdateView):
    model = Sale

    fields = ['client']

    success_url = reverse_lazy('salesList')

class SaleDelete(DeleteView):
    model = Sale

    slug_field = 'name'
    slug_url_kwarg = 'name'

    success_url = reverse_lazy('salesList')