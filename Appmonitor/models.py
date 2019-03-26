from django.db import models

# Create your models here.

class port_stats(models.Model):
	device_id = models.TextField()
	port_id = models.IntegerField(primary_key=True)
	rx_packets = models.IntegerField()
	tx_packets = models.IntegerField()
	rx_dropped = models.IntegerField()
	tx_dropped = models.IntegerField()
	rx_errors = models.IntegerField()
	tx_errors = models.IntegerField()

class flow_stats(models.Model):
	length = models.IntegerField()
	table_id = models.TextField()
	duration_sec = models.IntegerField()
	priority = models.IntegerField()
	idle_timeout = models.IntegerField()
	hard_timeout = models.IntegerField()
	packet_count = models.IntegerField()
	