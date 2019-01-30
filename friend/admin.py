from django.contrib import admin

from .models import FriendRequest, Friend


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('request_user', 'response_user', )
    list_filter = ('request_user', 'response_user', )


class FriendAdmin(admin.ModelAdmin):
    list_display = ('request_user', 'response_user',)
    list_filter = ('request_user', 'response_user',)

admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Friend, FriendAdmin)