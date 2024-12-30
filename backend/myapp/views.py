from django.http import JsonResponse
from .models import Item

def get_items(request):
    try:
        # 모든 Item 객체 가져오기
        items = Item.objects.all()

        # Item 객체를 딕셔너리 리스트로 변환
        items_data = [
            {
                "id": item.id,  # 고유 식별자 추가
                "name": item.name,
                "quantity": item.quantity,
                "estimated_date": item.estimated_date.strftime('%Y-%m-%d')  # 날짜를 문자열로 변환
            }
            for item in items
        ]

        # JsonResponse로 반환
        return JsonResponse(items_data, safe=False)  # 리스트 반환 시 safe=False 설정 필요
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
