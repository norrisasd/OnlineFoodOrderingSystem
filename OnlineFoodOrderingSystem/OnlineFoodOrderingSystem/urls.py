"""OnlineFoodOrderingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from YamiFood import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
app_name='YamiFood'

urlpatterns = [
    path('',RedirectView.as_view(url='home', permanent=False), name='index_view'),
    path('admin/', admin.site.urls),
    path('home',views.IndexView.as_view(),name ="index_view"),
    path('contact',views.ContactView.as_view(),name ="contact_view"),
    path('about',views.AboutView.as_view(),name ="about_view"),
    path('order',views.OrderView.as_view(),name ="order_view"),
    path('features',views.FeaturesView.as_view(),name ="features_view"),
    path('login',views.LoginView.as_view(),name ="login_view"),
    path('signup',views.SignupView.as_view(),name ="signup_view"),
    path('dashboard',views.DashboardView.as_view(),name ="dashboard_view"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
