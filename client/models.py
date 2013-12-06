from django.db import models

# Create your models here.

# Este es el cliente que solicita el taxi.
# Por ahora, solo se
class Client(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	number = models.CharField(max_length=100, blank=True, null=True)
	device = models.OneToOneField('gcm.Device',null=True, blank=True)

	def __unicode__(self):
		return self.name
