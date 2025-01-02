from django.urls import path
from .views import get_buying_schedules, get_prediction_out
from . import views

urlpatterns = [
    path('api/prediction-out/', get_prediction_out, name='prediction-out'),
    path('api/buying-schedules/<int:medi_no>/', get_buying_schedules, name='buying-schedules'),
]
