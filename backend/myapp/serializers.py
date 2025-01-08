from rest_framework import serializers
from .models import Medicine, BuyingScheduling, PredictionOut

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'  # 모든 필드 직렬화

class BuyingSchedulingSerializer(serializers.ModelSerializer):
    medi_no = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all())  # ForeignKey 처리

    class Meta:
        model = BuyingScheduling
        fields = '__all__'  # 모든 필드 직렬화

class PredictionOutSerializer(serializers.ModelSerializer):
    medi_no = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all())  # ForeignKey 처리

    class Meta:
        model = PredictionOut
        fields = '__all__'  # 모든 필드 직렬화
