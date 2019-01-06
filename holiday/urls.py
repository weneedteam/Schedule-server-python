from django.urls import path

from .views import holiday_list


urlpatterns = [
    path('', holiday_list, name='holiday_list'),
]