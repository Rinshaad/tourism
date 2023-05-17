from rest_framework import serializers

from common.models import Admin, Customer

class Cuserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class Adminserializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
