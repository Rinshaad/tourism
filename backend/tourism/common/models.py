from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_phone = models.BigIntegerField()
    customer_address = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=30)
    customer_password = models.CharField(max_length=40, default='')
    status = models.CharField(max_length=20, default='active')

    class Meta:
        db_table = 'customer_tb'

class Admin(models.Model):
    admin_name = models.CharField(max_length=20)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=40, default='')

    class Meta:
        db_table = 'admin_tb'