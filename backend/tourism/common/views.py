from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Adminserializer, Cuserializer
from .models import Admin, Customer

# Create your views here.


@api_view(['POST'])
def admin_register(request):
    try:
        admin_data = request.data
        email_exist =  Admin.objects.filter(admin_email = admin_data['admin_email']).exists()
        msg = ''
        msg1 = ''
        
        if not email_exist:
            adminserialized_data = Adminserializer(data = admin_data)
            status = False
            
            msg1 = 'Email available'
            
            if adminserialized_data.is_valid():
                adminserialized_data.save()
                msg = 'Admin registered successfully'
            else:
                msg = 'Registration failed'
        else:
            status = True
            msg1 = 'Email already exist'
            return JsonResponse({'msg1':msg1})
    except:
        msg = 'Something went wrong'
        return JsonResponse({'msg': msg})
    return JsonResponse({'msg':msg, 'msg1':msg1,'email_exist': status})


@api_view(['POST'])
def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    try:
        check = Admin.objects.get(admin_email = username, admin_password = password)
        status = True
        print('mmmm')
        return JsonResponse ({'status':status,'token':check.id})
    except :
        status = False
    return JsonResponse ({'status':status})   

