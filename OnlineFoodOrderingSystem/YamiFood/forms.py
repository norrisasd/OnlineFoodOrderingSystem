from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class meta:
        model = Product
        fields = '__all__'