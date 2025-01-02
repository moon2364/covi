from django.urls import path
from .views import MedicineView, BuyingSchedulingView, PredictionOutView

urlpatterns = [
    path('api/medicines/', MedicineView.as_view(), name='medicine-list'),
    path('api/buying-schedules/<int:medi_no>/', BuyingSchedulingView.as_view(), name='buying-schedules'),
    path('api/prediction-out/', PredictionOutView.as_view(), name='prediction-out'),
]