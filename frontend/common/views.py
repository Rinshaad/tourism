from django.shortcuts import render

# Create your views here.

def base(request):
   
    return render(request,'common_templates/base.html')

def index(request):
   
    return render(request,'common_templates/index.html')

def blog(request):
   
    return render(request,'common_templates/blog.html')

def view_blog(request):
   
    return render(request,'common_templates/view_blog.html')

def aboutus(request):
   
    return render(request,'common_templates/aboutus.html')

def contactus(request):
   
    return render(request,'common_templates/contactus.html')


def customer_register(request):
   
    return render(request,'common_templates/customer_register.html')

def customer_login(request):
   
    return render(request,'common_templates/customer_login.html')

# /////////////// ADMIN //////////////////////

def admin_register(request):
   
    return render(request,'common_templates/admin_register.html')


def admin_login(request):
   
    return render(request,'common_templates/admin_login.html')


