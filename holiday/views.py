from django.shortcuts import render, HttpResponse

from .models import Holiday
from .get_holiday import get_api_data

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def holiday_list(request):
    data = get_api_data()

    return Response(data)