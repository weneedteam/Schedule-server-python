from rest_framework.routers import DefaultRouter

from .views import FriendRelationViewSet


router = DefaultRouter()
router.register('relation', FriendRelationViewSet)

urlpatterns = [

]

urlpatterns += router.urls