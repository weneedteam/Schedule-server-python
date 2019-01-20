from rest_framework.routers import DefaultRouter

from .views import FriendRequestViewSet


router = DefaultRouter()
router.register('request', FriendRequestViewSet)

urlpatterns = [

]

urlpatterns += router.urls