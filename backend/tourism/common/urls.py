from django.urls import path
from . import views

app_name = 'common'


urlpatterns = [
    # path('customer_register/',views.customer_register),
    # path('customer_login/',views.customer_login),
    path('admin_register/',views.admin_register),
    path('admin_login/',views.admin_login),
    
]
