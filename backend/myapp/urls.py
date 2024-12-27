from django.urls import path
from . import views

urlpatterns = [
    path('medicine/<str:name>/', views.show_medicine, name='show_medicine'),
    path('', views.main),
]
