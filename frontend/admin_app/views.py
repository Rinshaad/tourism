from django.shortcuts import render

# Create your views here.
def base(request):
   return render(request,'admin_app_templates/base.html')

def admin_dashboard(request):
   return render(request,'admin_app_templates/admin_dashboard.html')

def all_customers(request):
   return render(request,'admin_app_templates/all_customers.html')

def add_description(request):
   return render(request,'admin_app_templates/add_description.html')

def view_destination(request):
   return render(request,'admin_app_templates/view_destination.html')

def view_booking(request):
   return render(request,'admin_app_templates/view_booking.html')

def view_queries(request):
   return render(request,'admin_app_templates/view_queries.html')

def change_password(request):
   return render(request,'admin_app_templates/change_password.html')