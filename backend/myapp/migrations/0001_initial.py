import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medi_no', models.AutoField(primary_key=True, serialize=False)),  # 의약품 ID
                ('medi_name', models.CharField(max_length=255)),  # 의약품 이름
                ('medi_name_detail', models.CharField(max_length=255, blank=True, null=True)),  # 의약품 이름 상세
                ('medi_standard', models.CharField(max_length=255, blank=True, null=True)),  # 표준 규격
                ('medi_packaging_type', models.CharField(max_length=255, blank=True, null=True)),  # 포장 형태
                ('medi_unit_qtt', models.IntegerField(blank=True, null=True)),  # 단위 수량
                ('medi_standard_code', models.CharField(max_length=50, blank=True, null=True)),  # 의약품 표준코드
                ('medi_insurance_status', models.CharField(max_length=50, blank=True, null=True)),  # 보험코드 구분
                ('medi_code', models.CharField(max_length=50, blank=True, null=True)),  # 의약품 제조코드
                ('medi_top_standard_code', models.CharField(max_length=50, blank=True, null=True)),  # 의약품 대표 표준코드
                ('pc_no', models.CharField(max_length=50, blank=True, null=True)),  # 제조사
                ('medi_main_ingredient_code', models.CharField(max_length=50, blank=True, null=True)),  # 주성분코드 (varchar로 변경)
            ],
            options={
                'db_table': 'medicine',
            },
        ),
        
        migrations.CreateModel(
            name='BuyingScheduling',
            fields=[
                ('buying_id', models.AutoField(primary_key=True, serialize=False)),
                ('prediction_qtt', models.BigIntegerField(blank=True, null=True)),
                ('medi_name', models.CharField(max_length=255, blank=True, null=True)),
                ('medi_standard', models.CharField(max_length=255, blank=True, null=True)),
                ('medi_packaging_type', models.CharField(max_length=255, blank=True, null=True)),
                ('prediction_dt', models.DateField(blank=True, null=True)),
                ('prediction_pharm', models.CharField(max_length=255, blank=True, null=True)),
                ('pharm_per_qtt', models.BigIntegerField(blank=True, null=True)),
                ('order_prob', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('medi_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buying_schedules', to='myapp.medicine')),
            ],
            options={
                'db_table': 'buying_scheduling',
            },
        ),
        
        migrations.CreateModel(
            name='PredictionOut',
            fields=[
                ('prediction_no', models.AutoField(primary_key=True, serialize=False)),
                ('prediction_qtt', models.BigIntegerField(blank=True, null=True)),
                ('medi_name', models.CharField(max_length=255, blank=True, null=True)),
                ('medi_standard', models.CharField(max_length=255, blank=True, null=True)),
                ('medi_packaging_type', models.CharField(max_length=255, blank=True, null=True)),
                ('amount', models.BigIntegerField(blank=True, null=True)),
                ('ms_rt_unit_price', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('mileage', models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)),
                ('medi_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prediction_outs', to='myapp.medicine')),
            ],
            options={
                'db_table': 'prediction_out',
            },
        ),
    ]
