from django import forms

class addCategoryForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-muted'}), label='Category name')

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=200)
    file = forms.FileField(required=False)

class addCategoryValueForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-muted'}), label='Category value name')

