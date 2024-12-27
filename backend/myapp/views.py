from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Medicine

def show_medicine(request, name):
    try:
        medicine = Medicine.objects.get(name=name)  # 특정 이름의 약 가져오기
        return render(request, 'medicine_detail.html', {'medicine': medicine})
    except Medicine.DoesNotExist:
        return render(request, 'medicine_detail.html', {'error': '해당 이름의 약이 존재하지 않습니다.'})

def main(request):
    message = request.GET.get('medicine')
    # try:
    # Medicine 객체 가져오기
    medicine = Medicine.objects.get(name=message)

    # 딕셔너리로 데이터 구성
    medicine_data = {
        "name": medicine.name,
        "quantity": medicine.quantity,
        "prob": str(medicine.prob),  # Decimal 값을 문자열로 변환
    }

    # JsonResponse로 반환
    return JsonResponse(medicine_data)
    # except :
    #     return JsonResponse({"error": "해당 이름의 약이 존재하지 않습니다."}, status=404)