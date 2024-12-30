from django.db import models

# Create your models here.

# 품목 수량 예상일자 테이블
class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)  # 품목 이름
    quantity = models.IntegerField(blank=False)  # 수량
    estimated_date = models.DateField(blank=False)  # 주문 예상 일자

    class Meta:
        db_table = 'item'  # 테이블 이름

    def __str__(self):
        return self.name


# 품목별 약국 정보 테이블
class PharmacyOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='pharmacy_orders')  # 품목
    pharmacy_name = models.CharField(max_length=100, blank=False)  # 약국 이름
    quantity = models.IntegerField(blank=False)  # 수량
    order_probability = models.DecimalField(max_digits=5, decimal_places=2, blank=False)  # 주문 확률 (%)

    class Meta:
        db_table = 'pharmacy_order'  # 테이블 이름

    def __str__(self):
        return f"{self.item.name} - {self.pharmacy_name}"
