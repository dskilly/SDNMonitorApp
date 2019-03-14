from django.http import HttpResponse

from .models import *

def logs(request):
	logs = Log_Message.objects.values_list('syslog', flat=True)
	response = 'Logs for the SDN Controller:<br />'
	response += '<br />'.join([x for x in logs]) if len(logs) > 0 else 'No logs...'
	return HttpResponse(response)