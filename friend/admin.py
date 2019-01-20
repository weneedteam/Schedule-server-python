from django.contrib import admin

from .models import FriendRequest


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('request_user', 'response_user', 'assent', )
    list_filter = ('request_user', 'response_user', )


admin.site.register(FriendRequest, FriendRequestAdmin)