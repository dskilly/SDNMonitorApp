from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(port_stats)
admin.site.register(flow_stats)
admin.site.register(desc_stats)
admin.site.register(table_stats)
admin.site.register(queue_stats)