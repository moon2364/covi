from django.contrib import admin
from .models import Medicine
from .models import Item, PharmacyOrder

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'estimated_date']  # 관리 페이지에 표시될 필드
    search_fields = ['name']  # 검색 필드
    list_filter = ['estimated_date']  # 필터링 가능한 필드


@admin.register(PharmacyOrder)
class PharmacyOrderAdmin(admin.ModelAdmin):
    list_display = ['item', 'pharmacy_name', 'quantity', 'order_probability']  # 관리 페이지에 표시될 필드
    search_fields = ['pharmacy_name', 'item__name']  # 검색 필드 (ForeignKey는 item__name으로 접근)
    list_filter = ['pharmacy_name']  # 필터링 가능한 필드
    
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'prob']  # 관리 페이지에 표시될 필드
