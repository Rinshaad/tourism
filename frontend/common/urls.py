from django.urls import path
from . import views
app_name='common'


urlpatterns=[
    path('base',views.base,name='base'),
    path('',views.index,name='home'),
    path('blog',views.blog,name='blog'),
    path('view_blog',views.view_blog,name='view_blog'),
    path('aboutus',views.aboutus,name='about'),
    path('contactus',views.contactus,name='contact'),
    path('customer_register/',views.customer_register,name='customer_register'),
    path('customer_login/',views.customer_login,name='customer_login'),
    path('admin_register/',views.admin_register,name='admin_register'),
    path('admin_login/',views.admin_login,name='admin_login'),
]