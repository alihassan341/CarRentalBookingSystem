from django.contrib import admin
from django.urls import path
from CarRentalBooking import views

urlpatterns = [
    path('', views.Home,name= 'Home'),
    
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