from django.urls import path
from .views import get_buying_schedules, get_prediction_out
from . import views

urlpatterns = [
    path('api/buying-schedules/', get_buying_schedules, name='buying-schedules'),
    path('api/prediction-out/<int:item_id>/', get_prediction_out, name='prediction-out'),
]
