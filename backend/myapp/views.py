from django.http import JsonResponse
from .models import  BuyingScheduling, PredictionOut

def get_buying_schedules(request):
    try:
        # 모든 BuyingScheduling 객체 가져오기
        schedules = BuyingScheduling.objects.all()

        # BuyingScheduling 객체를 딕셔너리 리스트로 변환
        schedules_data = [
            {
                "id": schedule.table_id,  # 고유 식별자
                "name": schedule.medi_name,  # 의약품 이름
                "quantity": schedule.prediction_qtt,  # 예측 수량
                "estimated_date": schedule.prediction_dt.strftime('%Y-%m-%d')  # 예상 일자
            }
            for schedule in schedules
        ]

        # JsonResponse로 반환
        return JsonResponse(schedules_data, safe=False)  # 리스트 반환 시 safe=False 설정 필요
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

def get_prediction_out(request, item_id):
    try:
        # 선택된 품목(Item)에 해당하는 예측 결과 가져오기
        prediction_results = PredictionOut.objects.filter(medi_no=item_id)

        # 데이터를 딕셔너리 리스트로 변환
        prediction_data = [
            {
                "id": result.prediction_no,  # 예측 ID
                "name": result.medi_name,  # 의약품 이름
                "quantity": result.amount,  # 재고 수량
                "unit_price": float(result.ms_rt_unit_price),  # 단가 (소수점 변환)
            }
            for result in prediction_results
        ]

        # JsonResponse로 반환
        return JsonResponse(prediction_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)