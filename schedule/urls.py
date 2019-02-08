from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ScheduleViewSet


router = DefaultRouter()

router.register('schedule', ScheduleViewSet)


urlpatterns = [

]


urlpatterns += router.urls