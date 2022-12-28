from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request,"index.html")

def About(request):
    return render(request,'about.html') 

def Register(request):
    return render(request,'Signup.html') 

# def Login(request):
#     return render(request,'about.html') 

def ContactUs(request):
    return render(request,'contact.html') 

def service (request):
    return render(request,'service.html')

def booking (request):
    return render(request,'booking.html')

def account (request):
    return render(request,'my-account.html')
    
def myorders (request):
    return render(request,'my-orders.html')

def payment(request):
    return render(request,'my-payment.html')

def privacypolicy(request):
    return render(request,'privacy-policy.html')

def myaccountdetails(request):
    return render (request,'my-account-details')



