from dataclasses import fields
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


class CustomerOrderSerilizer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id','customer_name','email','mobile_number','city','order']

    def get_order(self, obj):
            orders = Order.objects.filter(
                customer=obj.id)
            serializer = OrderSerilizer(orders, many=True)
    
            return serializer.data

class CustomerOrderShippingSerilizer(serializers.ModelSerializer):
    Customer = serializers.SerializerMethodField()
    shipping = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['Customer','id','customer','product_name','quantity','pricing','mrp','shipping']

    def get_Customer(self, obj):
            customers = Customer.objects.filter(
                id = obj.customer.id)
            serializer = CustomerSerilizer(customers, many=True)
    
            return serializer.data

    def get_shipping(self, obj):
            shipping = Shipping.objects.filter(
                purchase_order = obj.id)
            serializer = ShippingSerilizer(shipping, many=True)
    
            return serializer.data
