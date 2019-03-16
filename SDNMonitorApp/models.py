from django.db import models

class total_traffic(models.Model):
	total_rx_bytes = models.IntegerField(default=0)
	total_tx_bytes = models.IntegerField(default=0)
	ts = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}, {}'.format(self.total_rx_bytes, self.total_tx_bytes)

class Log_Message(models.Model):
	device_id = models.TextField(null=True, blank=True)
	syslog = models.TextField()
	ts = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.syslog

class nodes_table(models.Model):
	id = models.TextField()
	created = models.DateTimeField()
	modified = models.DateTimeField()
	label = models.TextField()

	def __str__(self):
		return self.label

class links_table(models.Model):
	id = models.TextField()
	created = models.DateTimeField()
	modified = models.DateTimeField()
	cost = models.IntegerField()
	status = models.BooleanField()
	source_id = models.TextField()
	target_id = models.TextField()
	status_changed = models.DateTimeField()

	def __str__(self):
		return 'link: {} -> {}'.format(self.source_id, self.target_id)