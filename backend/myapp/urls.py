from django.urls import path
from .views import get_items
from . import views

urlpatterns = [
    path('api/items/', get_items, name='item-list'),  # API URL 설정,
]
