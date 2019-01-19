from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from .models import User, FriendRelation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NickNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nick_name', )


class FriendRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRelation
        fields = '__all__'