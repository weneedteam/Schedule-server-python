from django.contrib import admin

from .models import Holiday


class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'month', 'day', 'created_at', )
    list_filter = ('name', 'year', )

admin.site.register(Holiday, HolidayAdmin)