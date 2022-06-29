
from django.shortcuts import render
from .models import Customer, Order, Shipping
from django.http import JsonResponse
from .serializers import CustomerSerilizer, OrderSerilizer, ShippingSerilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def customer_view(request):

    if request.method == 'GET':
        customers=Customer.objects.all()
        serializer = CustomerSerilizer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = CustomerSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def purchase_order(request):
    if request.method == 'GET':
        customers=Order.objects.all()
        serializer = OrderSerilizer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = OrderSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def purchase_order(request):
    if request.method == 'GET':
        customers=Shipping.objects.all()
        serializer = ShippingSerilizer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = ShippingSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    