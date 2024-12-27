from django.shortcuts import render
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
    medicine = Medicine.objects.get(name=message)
    lst = [medicine.name, medicine.quantity, medicine.prob]
    return HttpResponse(lst)