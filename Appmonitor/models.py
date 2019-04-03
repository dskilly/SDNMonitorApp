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
	table_id = models.TextField()
	duration_sec = models.IntegerField()
	priority = models.IntegerField()
	idle_timeout = models.IntegerField()
	hard_timeout = models.IntegerField()
	packet_count = models.IntegerField()

class desc_stats(models.Model):
	mfr_desc = models.TextField()
	hw_desc = models.TextField()
	sw_desc = models.TextField()
	serial_num = models.TextField()
	dp_desc = models.TextField()

class table_stats(models.Model):
	table_id = models.TextField(primary_key=True)
	name = models.TextField()
	wildcards = models.IntegerField()
	max_entries = models.IntegerField()
	active_count = models.IntegerField()
	lookup_count = models.IntegerField()
	matched_count = models.IntegerField()

class queue_stats(models.Model):
	port_no = models.IntegerField()
	queue_id = models.IntegerField()
	tx_bytes = models.IntegerField()
	tx_packets = models.IntegerField()
	tx_errors = models.IntegerField()