import logging

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from .forms import *
from .models import Contact

_logger = logging.getLogger('django')

# Create your views here.
class ContactsList(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.all().order_by('name')

class ContactCreate(TemplateView):
    template_name = 'contact_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()

        return context

def executeContactCreate(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                street = form.cleaned_data['street'],
                city = form.cleaned_data['city'],
                code = form.cleaned_data['code'],
            )
            contact.save()
            return redirect('contactsList')
        else:
            return redirect('contactCreate')
    else:
        return redirect('contactCreate')


class ContactDetail(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'

    def get_queryset(self):
        return Contact.objects.filter(id=self.kwargs['pk'])

class ContactDetailEdit(TemplateView):
    template_name = 'contact_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(id=self.kwargs['pk'])
        return context

def contactEditExecute(request, pk):
    if request.method == "POST":
        form = ContactForm(request.POST)
        _logger.info("FED INFO")
        if form.is_valid():
            contact = Contact.objects.get(id=pk)
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.street = form.cleaned_data['street']
            contact.city = form.cleaned_data['city']
            contact.code = form.cleaned_data['code']
            contact.save()

            return redirect('contactDetail', pk=pk)
        else:
            return redirect('editContact', pk=pk)
    else:
        return redirect('editContact', pk=pk)

class ContactDelete(TemplateView):
    template_name = 'contact_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(id=self.kwargs['pk'])
        return context

def contactDeleteExecute(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('contactsList')