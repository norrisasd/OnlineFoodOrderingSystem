from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'./pages/index.html',{'nbar':'home'})

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