from django.db import models


# Create your models here.

class Customer(models.Model):
    #customer_id = models.CharField(max_length=6, primary_key=True, default=pkgen)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    pricing = models.IntegerField()
    mrp = models.IntegerField()

class Shipping(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    purchase_order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=50)


    
