from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import port_stats, flow_stats


# Create your views here.

def Appmonitorsite(request):
	devices = port_stats.objects.values('device_id').distinct()
	nodes = [{name: x.device_id, tx_errors: sum([y.tx_errors for y in port_stats.objects.filter(device_id=x.device_id)])} for x in nodes]
	return render(request,'Appmonitor/Appmonitorsite.html', {'nodes': nodes, 'flows': flow_stats.objects.all()})
