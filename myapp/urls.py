from django.urls import path
from . import views

urlpatterns = [
    path('customer/',views.customer_view),
    path('order/',views.purchase_order),
    path('shipping/',views.purchase_order),
    path('shipping/<str:city>', views.CityView.as_view()),
    path('customer_orders/',views.customer_purchase),
    #path('customer_orders_shipping/',views.customer_purchase_shipping),
]

