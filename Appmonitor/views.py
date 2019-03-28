from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import port_stats, flow_stats


# Create your views here.

def Appmonitorsite(request):
	devices = port_stats.objects.values('device_id').distinct()
	nodes = []
	for device in devices:
		name = device['device_id']
		nodes.append({'name': name, 'tx_errors': sum([x.tx_errors for x in port_stats.objects.filter(device_id=name)])})
	return render(request,'Appmonitor/Appmonitorsite.html', {'nodes': nodes, 'flows': flow_stats.objects.all()})
