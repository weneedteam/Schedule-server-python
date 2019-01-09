from django.urls import path

from .views import HolidayViewSet
from .views import holiday_list

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('holiday-list', HolidayViewSet)


urlpatterns = [
    path('', holiday_list, name='holiday_list'),
]


urlpatterns += router.urls