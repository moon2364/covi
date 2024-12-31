import os
import django

# Django 환경 초기화
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # 프로젝트에 맞게 수정
django.setup()  # Django 앱 초기화

from django.contrib.auth.models import User

# Superuser 정보 가져오기
username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "adminpassword")

# Superuser 생성
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created.")
else:
    print(f"Superuser '{username}' already exists.")
