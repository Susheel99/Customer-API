from django.urls import path
from . import views

urlpatterns = [
    path('customer/',views.customer_view),
    path('order/',views.purchase_order),
    path('shipping/',views.purchase_order),
    path('shipping/<str:city>', views.CityView.as_view()),
]

