from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content')
    list_filter = ('owner',)
    list_per_page = 15

admin.site.register(Message, MessageAdmin)
