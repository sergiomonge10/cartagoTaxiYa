from django.db import models
from client.models import Client
from company.models import Company

#Este es el taxista o conductor
class Driver(models.Model):
	nid = models.CharField(max_length=20)
	password = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	phone = models.CharField(max_length=20)
	enable = models.BooleanField(default=True)
	company = models.ForeignKey(Company)
	car =  models.ManyToManyField('Car',null=True, blank=True)
	device = models.OneToOneField('gcm.Device',null=True, blank=True)

	def __unicode__(self):
		return self.nid

#Este es el carro o el taxi
class Car(models.Model):
	number = models.CharField(max_length=20)
	type_car = models.ForeignKey('TypeCar',null=True, blank=True)
	reader_card = models.BooleanField(default=True)

	def __unicode__(self):
		return self.number

# Este es el tipo de carro, que puede ser
# para discapacitados, doble traccion, etc.
class TypeCar(models.Model):
	name = models.CharField(max_length=30)
	enable = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

#Una ruta relaciona a un taxi, un taxista.
class Route(models.Model):
	client = models.ForeignKey(Client)
	driver = models.ForeignKey('Driver')
	date = models.DateTimeField(auto_now_add=True)
	enable = models.BooleanField(default=True)
	origin = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)

	def __unicode__(self):
		return self.driver

class DriverLocation(models.Model):
	driver = models.OneToOneField('Driver')
	latitude = models.CharField(max_length=300)
	longitude = models.CharField(max_length=300)
	city = models.CharField(max_length=300)
	country = models.CharField(max_length=300)

	def __unicode__(self):
		return self.driver.name

class Driver_Decision(models.Model):
	driver = models.OneToOneField('Driver')
	decision = models.BooleanField(default=False)

	def __unicode__(self):
		return self.driver.name
		