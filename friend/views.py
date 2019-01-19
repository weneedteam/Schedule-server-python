from django.shortcuts import render

from .models import FriendRelation

from .serializers import FriendRelationSerializer

from rest_framework import viewsets


class FriendRelationViewSet(viewsets.ModelViewSet):
    queryset = FriendRelation.objects.all()
    serializer_class = FriendRelationSerializer