from django.contrib import admin

from .models import Detail


class DetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'duration', 'end', 'ip')
    list_editable = ('ip',)
    list_filter = ('name',)
    empty_value_display = '暂无数据'
    list_per_page = 15


admin.site.register(Detail, DetailAdmin)
