from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class FriendRelation(models.Model):
    request_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='request_user')
    response_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='response_user')
    assent = models.IntegerField(blank=True, default=0)
    assented_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)