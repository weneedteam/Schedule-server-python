from django.urls import path

from rest_framework.routers import DefaultRouter

from djoser.urls import urlpatterns

from .views import user_create, NickNameViewSet

router = DefaultRouter()

router.register('nick-name', NickNameViewSet)

urlpatterns = [
    path('signup', user_create, name="user-create"),
]

urlpatterns += router.urls