from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)  # 일정 추가자
    title = models.CharField(max_length=300)  # 일정 타이틀
    state = models.IntegerField()  # 일정 상태(?)
    start_time = models.DateTimeField()  # 일정 시간
    latitude = models.FloatField()  # 일정 장소 - 위도
    longitude = models.FloatField()  # 일정 장소 - 경도
    content = models.TextField()  # 일정 설명