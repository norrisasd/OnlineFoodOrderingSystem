from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.base import RedirectView
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
cart = Order_Details.objects.get_queryset().select_related("product_id",'order_id').filter(order_id__status=0)
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


class OrderView(View):
    def get(self,request):
        zcart = Order_Details.objects.get_queryset().select_related("product_id",'order_id').filter(order_id__status=0)
        products = Product.objects.all()
        if request.is_ajax():
            if request.GET.get("request") == "getMyCart":
                mycart = serializers.serialize('json', list(zcart))
                prod = serializers.serialize('json', list(products))
                return JsonResponse({'cart':mycart,'products':prod},status=200)
            return JsonResponse({'products':products},status=200)
        return render(request,'./pages/menu.html',{'nbar':'order','products':products})
    def post(self,request):
        if request.POST.get("request") == "addToCart":
            form = OrderDetailsForm(request.POST)
            product = request.POST.get("product_id")
            form = Order_Details(quantity = 0,order_id_id = 1,product_id_id = product)
            form.save()
            return JsonResponse({'check':True},status=200)


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
        form = UserForm(request.POST)
        if form.is_valid() and request.POST.get("signup") == "register":
            username = request.POST.get("username")
            password = request.POST.get("password")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone_number = request.POST.get("phone_number")
        form = User(username = username, password = password, first_name = first_name, last_name = last_name, 
                    phone_number = phone_number, is_admin = False)
        form.save()
        return redirect('./home')

class DashboardView(View):
    def get(self,request):
        users = User.objects.all()
        products = Product.objects.all()
        orders = Order.objects.all()
        deliveries = Delivery.objects.all()
        context = {
            'users': users,
            'products': products,
            'orders': orders,
            'deliveries': deliveries,
            'nbar':'dashboard',
            'carts':cart
        }
        if request.is_ajax(): 
            data = serializers.serialize('json', list(products))
            return JsonResponse({'products':data},status=200)
                
                
        return render(request,'./pages/dashboard.html', context)  

    def post(self,request):
        Pform = ProductForm(request.POST)
        Uform= UserForm(request.POST)
        #Product Add
        if request.is_ajax():
            if request.POST.get("product_name") != "":
                file = request.FILES["product_picture"]
                name=request.POST.get("product_name")
                category =request.POST.get("category")
                price =request.POST.get("price")
                picture =file.name
                Pform = Product(product_name=name,product_category=category,product_picture=picture,price=price)
                fs = FileSystemStorage()
                fs.save(file.name,file)
                Pform.save()
            elif request.POST.get("username") != "":
                username = request.POST.get('username')
                password = request.POST.get('password')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                phone_number = request.POST.get('phone_number')
                Uform = User(username = username, password = password, first_name = first_name, last_name = last_name, phone_number = phone_number, is_admin = True)
                Uform.save()
            return JsonResponse({'status':True},status=200)
        else:
            return JsonResponse({'status':False},status=200)
