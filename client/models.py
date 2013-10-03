from django.db import models

# Create your models here.

# Este es el cliente que solicita el taxi.
# Por ahora, solo se
class Client(models.Model):
	name = models.CharField(max_length=100, default='Ano', blank=True, null=True)

	def __unicode__(self):
		return self.name
