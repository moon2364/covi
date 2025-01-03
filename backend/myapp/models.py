from django.db import models

# Create your models here.


class Medicine(models.Model):
    medi_no = models.AutoField(primary_key=True)  # 의약품 ID
    medi_name = models.CharField(max_length=255)  # 의약품 이름
    medi_name_detail = models.CharField(max_length=255, blank=True, null=True)  # 의약품 이름 상세
    medi_standard = models.CharField(max_length=255, blank=True, null=True)  # 표준 규격
    medi_packaging_type = models.CharField(max_length=255, blank=True, null=True)  # 포장 형태
    medi_unit_qtt = models.IntegerField(blank=True, null=True)  # 단위 수량
    medi_standard_code = models.CharField(max_length=50, blank=True, null=True)  # 의약품 표준코드
    medi_insurance_status = models.CharField(max_length=50, blank=True, null=True)  # 보험코드 구분 (Y급여/N비급여)
    medi_code = models.CharField(max_length=50, blank=True, null=True)  # 의약품 제조코드 (ITCO)
    medi_top_standard_code = models.CharField(max_length=50, blank=True, null=True)  # 의약품 대표 표준코드
    pc_no = models.CharField(max_length=50, blank=True, null=True)  # 제조사
    medi_main_ingredient_code = models.CharField(max_length=50, blank=True, null=True)  # 주성분코드 (varchar로 변경)

    class Meta:
        db_table = 'medicine'  # 테이블 이름
        verbose_name = '의약품 정보'
        verbose_name_plural = '의약품 정보'

    def __str__(self):
        return self.medi_name
    
class BuyingScheduling(models.Model):
    buying_id = models.AutoField(primary_key=True)  # 테이블 ID
    medi_no = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='buying_schedules')  # 의약품 ID (ForeignKey)
    prediction_qtt = models.BigIntegerField(blank=True, null=True)  # 예측 수량
    medi_name = models.CharField(max_length=255, blank=True, null=True)  # 의약품 이름
    medi_standard = models.CharField(max_length=255, blank=True, null=True)  # 표준 규격
    medi_packaging_type = models.CharField(max_length=255, blank=True, null=True)  # 포장 형태
    prediction_dt = models.DateField(blank=True, null=True)  # 예상 일자
    prediction_pharm = models.CharField(max_length=255, blank=True, null=True)  # 예상 약국
    pharm_per_qtt = models.BigIntegerField(blank=True, null=True)  # 약국별 수량
    order_prob = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 주문 확률

    class Meta:
        db_table = 'buying_scheduling'
        verbose_name = '사입 스케줄링'
        verbose_name_plural = '사입 스케줄링'

    def __str__(self):
        return f"Buying Scheduling ({self.table_id}): {self.medi_name}"
    
class PredictionOut(models.Model):
    prediction_no = models.AutoField(primary_key=True)  # 예측 ID
    medi_no = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='prediction_outs')  # 의약품 ID (ForeignKey)
    prediction_qtt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 예측 수량
    medi_name = models.CharField(max_length=255, blank=True, null=True)  # 의약품 이름
    medi_standard = models.CharField(max_length=255, blank=True, null=True)  # 표준 규격
    medi_packaging_type = models.CharField(max_length=255, blank=True, null=True)  # 포장 형태
    amount = models.BigIntegerField(blank=True, null=True)  # 재고 수량
    ms_rt_unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 단가
    mileage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 마일리지

    class Meta:
        db_table = 'prediction_out'
        verbose_name = '예측 결과'
        verbose_name_plural = '예측 결과'

    def __str__(self):
        return f"PredictionOut ({self.prediction_no}): {self.medi_name}"