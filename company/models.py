from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# La Company es la empresa a la que pertenece un grupo de
# taxis y taxistas.
class Company(models.Model):
	name = models.CharField(max_length=100)
	user = models.OneToOneField(User)
	logo = models.ImageField(upload_to='logos', blank=True)
	phone = models.CharField(max_length=30, null=True, blank=True)
	city = models.CharField(max_length=30, null=True, blank=True)
	country = models.CharField(max_length=30)
	email = models.EmailField(blank=True, null=True)
	enable = models.BooleanField(default=True)

	def __unicode__(self):
		#return u"Nombre:  %s - Usuario: %s " % (self.name, self.user.username)
		return self.name
