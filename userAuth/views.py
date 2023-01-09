from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegistrationUserForm
from django.core.mail import send_mail
# Create your views here.
import logging
_logger = logging.getLogger('django')
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class LoginView(TemplateView):
    template_name = 'login.html'

def loginExecute(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
            # return HttpResponseRedirect(reverse('homePage'))
        else:
            messages.success(request, ("There was an error logging in, try again"))
            return HttpResponseRedirect(reverse('loginView'))
    else:
        return HttpResponseRedirect(reverse('loginView'))

class RegisterView(TemplateView):
    template_name = 'register.html'

def registerExecute(request):
    if request.method == "POST":
        _logger.info(request.POST)
        form = RegistrationUserForm(request.POST)
        _logger.info(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful"))
            return redirect('homePage')
        else:
            return redirect('registerView')
    else:
        return redirect('registerView')

class RecoverPassword(TemplateView):
    template_name = 'recoverPassword.html'

def recoverExecute(request):
    pass

class ForgotPassword(TemplateView):
    template_name = 'forgotPassword.html'

def forgotPassExecute(request):
    send_mail(
        'TEST',
        'You forgot your password, you dumb piece of shit',
        'pawelrosa686@gmail.com',
        ['pawelrosa686@gmail.com'],
        fail_silently=False,
    )