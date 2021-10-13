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
class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order_Details
        fields = ('quantity','order_id','product_id')

class CarrierForm(forms.ModelForm):
    class Meta:
        model = Delivery 
        fields = ('delivery_carrier',)

