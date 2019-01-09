from django.db import models

# Create your models here.
class Holiday(models.Model):
    name = models.CharField(max_length=100)  # 공휴일 이름
    year = models.IntegerField()  # 공휴일 년도
    month = models.IntegerField()  # 공휴일 월
    day = models.IntegerField()  # 공휴일 일
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜 
    updated_at = models.DateTimeField(auto_now=True)  # 수정 날짜

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('year', 'month', 'day', )