from django.urls import path
from .views import get_items
from .views import get_pharmacy_orders
from . import views

urlpatterns = [
    path('api/items/', get_items, name='item-list'),  # API URL 설정,
    path('api/pharmacy-orders/<int:item_id>/', get_pharmacy_orders, name='pharmacy-orders'),
]
