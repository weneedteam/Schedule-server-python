from rest_framework.routers import DefaultRouter

from .views import FriendRequestViewSet, FriendViewSet


router = DefaultRouter()
router.register('request', FriendRequestViewSet)
router.register('list', FriendViewSet)

urlpatterns = [

]

urlpatterns += router.urls