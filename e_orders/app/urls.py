from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClientListCreateView, OrderListCreateView

router = DefaultRouter()
router.register(r"clients", ClientListCreateView, basename="client")
router.register(r"orders", OrderListCreateView, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
