from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

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


#
#Tables for topology information
#

class nodes_table(models.Model):
	id = models.TextField(primary_key=True)
	created = models.DateTimeField()
	modified = models.DateTimeField()
	label = models.TextField()

	def __str__(self):
		return self.label

class links_table(models.Model):
	id = models.TextField(primary_key=True)
	created = models.DateTimeField()
	modified = models.DateTimeField()
	cost = models.IntegerField()
	STATUS = Choices('up', 'down', 'congested')
	status = StatusField()
	source_id = models.TextField()
	target_id = models.TextField()
	status_changed = models.DateTimeField()

	def __str__(self):
		return 'link: {} -> {}'.format(self.source_id, self.target_id)