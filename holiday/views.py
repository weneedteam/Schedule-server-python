from django.shortcuts import render

from .models import Holiday
from .get_holiday import get_api_data


def holiday_list(request):
    data = get_api_data()