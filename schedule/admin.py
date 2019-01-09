from django.contrib import admin

from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'latitude', 'longitude', )
    list_filter = ('title', 'user', )


admin.site.register(Schedule, ScheduleAdmin)