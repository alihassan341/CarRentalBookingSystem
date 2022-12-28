"""CarRentalBookingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from CarRentalBookingSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('About', views.About,name= 'About'),

    path('Contact', views.ContactUs,name= 'ContactUs'),

    path('Signup', views.Register,name= 'Register'),

    # path('Login', views.Login,name= 'Login'),

    path('service', views.service,name= 'service'),

    path('account', views.account,name= 'account'),
     
    path('booking', views.booking,name= 'booking'),

    path('orders',views.myorders,name='orders'),

    path("payment", views.payment, name="my-payment"),

    
    path("privacy-policy", views.payment, name="privacy"),
     

    
    

     
   
]
