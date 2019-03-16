from django.contrib import admin

from .models import *

admin.site.register(total_traffic)
admin.site.register(Log_Message)
admin.site.register(nodes_table)
admin.site.register(links_table)