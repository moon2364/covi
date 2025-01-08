from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medicine, BuyingScheduling, PredictionOut
from .serializers import MedicineSerializer, BuyingSchedulingSerializer, PredictionOutSerializer

# Medicine View
class MedicineView(APIView):
    def get(self, request):
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Buying Scheduling View
class BuyingSchedulingView(APIView):
    def get(self, request, medi_no):
        schedules = BuyingScheduling.objects.filter(medi_no=medi_no)
        serializer = BuyingSchedulingSerializer(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# PredictionOut View
class PredictionOutView(APIView):
    def get(self, request):
        predictions = PredictionOut.objects.all()
        serializer = PredictionOutSerializer(predictions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
