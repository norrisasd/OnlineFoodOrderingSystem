from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ('username','password','first_name','lastname','phone_number')

class ProductForm(forms.ModelForm):
    class meta:
        model = Product
        fields = '__all__'