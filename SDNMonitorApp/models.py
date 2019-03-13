from django.db import models

class total_traffic(models.Model):
	total_rx_bytes = models.IntegerField(default=0)
	total_tx_bytes = models.IntegerField(default=0)
	ts = models.DateTimeField(auto_now_add=True)

class Log_Message(models.Model):
	device_id = models.TextField(null=True, blank=True)
	syslog = models.TextField()
	ts = models.DateTimeField(auto_now_add=True)