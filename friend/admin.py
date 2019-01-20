from django.contrib import admin

from .models import FriendRelation


class FriendRelationAdmin(admin.ModelAdmin):
    list_display = ('request_user', 'response_user', 'assent', 'assented_at', )
    list_filter = ('request_user', 'response_user', )


admin.site.register(FriendRelation, FriendRelationAdmin)