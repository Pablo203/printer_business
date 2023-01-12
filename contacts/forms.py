from django import forms
from phone_field.forms import PhoneFormField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15)

    street = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))