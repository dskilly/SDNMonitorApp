from django.http import HttpResponse, JsonResponse

import json

from .models import *

def logs(request):
	logs = Log_Message.objects.values_list('syslog', flat=True)
	response = 'Logs for the SDN Controller:<br />'
	response += '<br />'.join([x for x in logs]) if len(logs) > 0 else 'No logs...'
	return HttpResponse(response)

def topology_request(request):
	topo = {
		'type': 'NetworkGraph',
		'protocol': 'openflow',
		'version': '1.0.0',
		'metric': '',
		'label': 'Topology for SDNMonitorApp',
	}
	topo['nodes'] = [{
		'id': x.id,
		'label': x.label
	} for x in nodes_table.objects.all()]
	topo['links'] = [{
		'source': x.source_id,
		'target': x.target_id,
		'cost': x.cost
	} for x in links_table.objects.all()]
	return JsonResponse(topo)