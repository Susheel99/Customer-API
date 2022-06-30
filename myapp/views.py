
from django.shortcuts import render
from .models import Customer, Order, Shipping
from django.http import JsonResponse
from .serializers import CustomerOrderSerilizer, CustomerOrderShippingSerilizer, CustomerSerilizer, OrderSerilizer, ShippingSerilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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
def shipping_details(request):
    if request.method == 'GET':
        customers=Shipping.objects.all()
        serializer = ShippingSerilizer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = ShippingSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CityView(APIView):
    def get(self, request, **kwargs):
       author = kwargs.get('city', None)
       address = Shipping.objects.all().filter(city=author).values()
       print(address[1])
       return JsonResponse({"Shipping Address": list(address)},safe=False)



@api_view(['GET'])
def customer_purchase(request):
    if request.method == 'GET':
        customers=Customer.objects.all()
        serializer = CustomerOrderSerilizer(customers, many=True)
        #print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def customer_purchase_shipping(request):
    if request.method == 'GET':
        orders=Order.objects.all()
        serializer = CustomerOrderShippingSerilizer(orders, many=True)
        #print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    
    