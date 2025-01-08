from django.contrib import admin
from .models import Medicine, BuyingScheduling, PredictionOut



@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        'medi_no',
        'medi_name',
        'medi_name_detail',
        'medi_standard',
        'medi_packaging_type',
        'medi_unit_qtt',
        'medi_standard_code',
        'medi_insurance_status',
        'medi_code',
        'medi_top_standard_code',
        'pc_no',
        'medi_main_ingredient_code',
    )
    search_fields = ('medi_name', 'medi_name_detail', 'medi_standard_code')
    # list_filter = ('medi_insurance_status', 'medi_packaging_type') # 필요한 필터 만들어서 확인
    
@admin.register(BuyingScheduling)
class BuyingSchedulingAdmin(admin.ModelAdmin):
    list_display = ['buying_id', 'medi_no', 'medi_name', 'prediction_qtt', 'prediction_dt', 'order_prob']  # 관리 페이지에 표시될 필드
    search_fields = ['medi_name', 'medi_no__medi_name']  # ForeignKey는 medi_no__medi_name으로 접근
    # list_filter = ['prediction_dt', 'medi_packaging_type']  # 필터링 가능한 필드


@admin.register(PredictionOut)
class PredictionOutAdmin(admin.ModelAdmin):
    list_display = ['prediction_no', 'medi_no', 'medi_name', 'prediction_qtt', 'amount', 'ms_rt_unit_price']  # 관리 페이지에 표시될 필드
    search_fields = ['medi_name', 'medi_no__medi_name']  # ForeignKey는 medi_no__medi_name으로 접근
    # list_filter = ['medi_standard', 'medi_packaging_type']  # 필터링 가능한 필드