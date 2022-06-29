from rest_framework import serializers
from .models import Customer, Order, Shipping

class CustomerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','customer_name','email','mobile_number','city']

class OrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','customer_id','product_name','quantity','pricing','mrp']

class ShippingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ['id','customer_id','address','city','pincode']
