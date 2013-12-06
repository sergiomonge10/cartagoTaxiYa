from django.contrib import admin
from cabbie.models import Driver, Car, TypeCar, Route, DriverLocation, Driver_Decision

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(TypeCar)
admin.site.register(Route)
admin.site.register(DriverLocation)
admin.site.register(Driver_Decision)