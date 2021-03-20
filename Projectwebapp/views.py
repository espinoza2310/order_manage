from django.shortcuts import render,HttpResponse
from servicesapp.models import Service

# Create your views here.

def home(request):
    
    return render(request,"Projectwebapp/home.html")

def services(request):
    services=Service.objects.all()
    return render(request,"Projectwebapp/services.html", {'services': services})

def shop(request):
    
    return render(request,"Projectwebapp/shop.html")

def blog(request):
    
    return render(request,"Projectwebapp/blog.html")

def contact(request):
    
    return render(request,"Projectwebapp/contact.html")


