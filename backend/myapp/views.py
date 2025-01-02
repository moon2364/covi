from django.http import JsonResponse
from .models import BuyingScheduling, PredictionOut

def get_prediction_out(request):
    try:
        # 모든 PredictionOut 객체 가져오기
        predictions = PredictionOut.objects.all()

        # PredictionOut 객체를 딕셔너리 리스트로 변환
        predictions_data = [
            {
                "id": prediction.prediction_no,  # 고유 식별자
                "medi_no" : prediction.medi_no.medi_no,
                "medi_name": prediction.medi_name,  # 의약품 이름
                "prediction_qtt": prediction.prediction_qtt,  # 예측 수량
                "amount": prediction.amount,  # 재고
            }
            for prediction in predictions
        ]

        # JsonResponse로 반환
        return JsonResponse(predictions_data, safe=False)  # 리스트 반환 시 safe=False 설정 필요
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def get_buying_schedules(request, medi_no):
    try:
        # 선택된 품목(Item)에 해당하는 BuyingScheduling 결과 가져오기
        schedules = BuyingScheduling.objects.filter(medi_no = medi_no)

        # 데이터를 딕셔너리 리스트로 변환
        schedules_data = [
            {
                "id": schedule.table_id,  # 사입 스케줄 ID
                "prediction_pharm": schedule.prediction_pharm,  # 약국 이름
                "pharm_per_qtt": schedule.pharm_per_qtt,  # 약국별 수량
                "prediction_dt": schedule.prediction_dt,  # BuyingScheduling에 단가 없음
                "order_prob": schedule.order_prob  # 주문 확률
            }
            for schedule in schedules
        ]

        # JsonResponse로 반환
        return JsonResponse(schedules_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
