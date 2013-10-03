from django.contrib import admin
from cabbie.models import Driver, Car, TypeCar, Route

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(TypeCar)
admin.site.register(Route)