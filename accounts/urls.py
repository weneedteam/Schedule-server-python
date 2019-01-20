from django.urls import path

from rest_framework.routers import DefaultRouter

from djoser.urls import urlpatterns

from .views import user_create, user_delete, set_password, set_username, user, NickNameViewSet


router = DefaultRouter()
router.register('users/nick-name', NickNameViewSet)

urlpatterns = [
    path('user/me', user, name='user'),
    path('user/signup', user_create, name="user-create"),
    path('user/delete', user_delete, name='user-delete'),
    path('user/email', set_username, name='set_username'),
    path('user/password', set_password, name='set_password'),
]

urlpatterns += router.urls