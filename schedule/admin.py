from django.contrib import admin

from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude', )
    list_filter = ('title', 'users', )


admin.site.register(Schedule, ScheduleAdmin)