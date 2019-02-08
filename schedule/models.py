from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class Schedule(models.Model):
    # user = models.ForeignKey(User, on_delete=models.PROTECT)  # 일정 추가자
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=300)  # 일정 타이틀
    state = models.IntegerField(default=0)  # 일정 상태(대기/시작/종료)
    start_time = models.DateTimeField()  # 일정 시간
    latitude = models.FloatField(blank=True, null=True)  # 일정 장소 - 위도
    longitude = models.FloatField(blank=True, null=True)  # 일정 장소 - 경도
    content = models.TextField(blank=True)  # 일정 설명

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('start_time', )