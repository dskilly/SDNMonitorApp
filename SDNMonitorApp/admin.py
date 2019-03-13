from django.contrib import admin

from .models import total_traffic, Log_Message

admin.site.register(total_traffic)
admin.site.register(Log_Message)