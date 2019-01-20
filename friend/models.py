from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class FriendRequest(models.Model):
    request_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='request_user_request')
    response_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='response_user_request')
    assent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Friend(models.Model):
    request_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='request_user_friend')
    response_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='response_user_friend')
    block = models.IntegerField()
    assented_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)