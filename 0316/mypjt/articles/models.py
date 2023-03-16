from django.db import models

# Create your models here.
"""
스키마 작성.
모델에 생긴 변화를 실제 DB에 반영 (migration)
명령어
1. makemigrations
모델에 생긴 변화를 마이그레이트로 만듬
2. migrate
데이터베이스에 반영시킴
"""
class Article(models.Model):  # 장고에서 제공하는 클래스 상속
    title = models.CharField(max_length=20)  # 텍스트 형식. 글자수 제한
    content = models.TextField()  #  텍스트형식. 글자수 제한 없음
    