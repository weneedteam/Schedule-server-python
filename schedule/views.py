from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ScheduleSerializer
from .models import Schedule


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer