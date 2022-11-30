from django import forms

class addCategoryForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-muted'}), label='Category name')