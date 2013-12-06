from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('client.views',

	url(r'^save/$', view="save_client"),

)