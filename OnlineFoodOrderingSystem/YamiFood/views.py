from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.base import RedirectView
from .forms import *

# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'./pages/index.html',{'nbar':'home'})

#About View
class AboutView(View):
    def get(self,request):
        return render(request,'./pages/about.html',{'nbar':'about'})

class ContactView(View):
    def get(self,request):
        return render(request,'./pages/contact.html',{'nbar':'contact'})

class MenuView(View):
    def get(self,request):
        return render(request,'./pages/menu.html',{'nbar':'menu'})

class FeaturesView(View):
    def get(self,request):
        return render(request,'./pages/features.html',{'nbar':'features'})

class LoginView(View):
    def get(self,request):
        return render(request,'./pages/login.html',{'nbar':'login'})

class SignupView(View):
    def get(self,request):
        return render(request,'./pages/signup.html',{'nbar':'signup'})

    def post(self, request):
        form= UserForm(request.POST)
        if form.is_valid():
            print("keke",request.POST)
        return redirect('./login')

class DashboardView(View):
    def get(self,request):
        users = User.objects.all()
        products = Product.objects.all()
        context = {
            'users': users,
            'products': products,
        }
        return render(request,'./pages/dashboard.html', context)
        