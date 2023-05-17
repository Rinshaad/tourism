from django.urls import path
from . import views
app_name='admin_app'


urlpatterns=[
    path('base',views.base,name='base'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('all_customers/',views.all_customers,name='all_customers'),
    path('add_description/',views.add_description,name='add_description'),
    path('view_destination/',views.view_destination,name='view_destination'),
    path('view_booking/',views.view_booking,name='view_booking'),
    path('view_queries/',views.view_queries,name='view_queries'),
    path('change_password/',views.change_password,name='change_password'),
]