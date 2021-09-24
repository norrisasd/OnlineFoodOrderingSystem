from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','phone_number','is_admin')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','product_category','product_picture','price')

