from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('cabbie.views',

	url(r'^add/driver/$',view="add_driver_view",name="add_driver"),
)