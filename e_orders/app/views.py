from rest_framework import viewsets

from .models import Client, Order
from .serializers import ClientSerializer, OrderSerializer


class ClientListCreateView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderListCreateView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
