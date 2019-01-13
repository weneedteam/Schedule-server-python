from django.urls import path

from .views import HolidayViewSet, HolidayListViewSet
# from .views import holiday_list

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('list', HolidayListViewSet, basename='list')
# router.register('list', HolidayViewSet)


urlpatterns = [
    # path('list/', holiday_list, name='holiday_list'),
]


urlpatterns += router.urls