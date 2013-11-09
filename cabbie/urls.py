from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('cabbie.views',

	url(r'^delete/(?P<nid>[-\w]+)/$', view='delete_driver_view',name='delete_driver'),

	url(r'^edit/car/(?P<number>[-\w]+)',view="edit_car_view",name="car"),
	url(r'^edit/driver/(?P<nid>[-\w]+)',view="edit_driver_view",name="edit_driver"),

	url(r'^types/$',view="get_types",name="types"),
	url(r'^drivers/$',view="get_drivers",name="drivers"),
	url(r'^add/car/$',view="add_car_view",name="add_car"),
	url(r'^add/driver/$',view="add_driver_view",name="add_driver"),
)