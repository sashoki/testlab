from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import Order, Customer


class OrderList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerList(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

