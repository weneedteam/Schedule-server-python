from rest_framework import serializers

from .models import FriendRelation


class FriendRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRelation
        fields = '__all__'