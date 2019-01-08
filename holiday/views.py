from django.shortcuts import render, HttpResponse

from .models import Holiday
from .get_holiday import get_api_data
from .serializers import HolidaySerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets


class HolidayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer


@api_view(['GET', 'POST'])
def holiday_list(request):
    # data = get_api_data()

    year = request.data['year']

    if not Holiday.objects.filter(year=year):
        holidays = get_api_data(year)
        serializer_list = []

        print(holidays)

        for holiday in holidays['results']:
            serializer = HolidaySerializer(data={
                "name": holiday['name'],
                "year": holiday['year'],
                "month": holiday['month'],
                "day": holiday['day'],
            })

            if serializer.is_valid():
                serializer.save()

                serializer_list.append(serializer.data)
            else:
                return Response({
                    "code": 409,
                    "message": "non-field-error",
                })

        return Response(serializer_list)
    else:
        datas = Holiday.objects.filter(year=year)
        # Todo: 일단 돌아가긴 하는데 dict 형태로 따로 한번 빼는게 맞는지 확인

        data_list = []

        for data in datas:
            json_data = {
                'name': data.name,
                'year': data.year,
                'month': data.month,
                'day': data.day,
            }

            data_list.append(json_data)

        return Response({
            'holidays': data_list,
        })