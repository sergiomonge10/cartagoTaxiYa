from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('company.views',

	url(r'^send/client/gcm/$',view="prueba_gcm"),
	url(r'^driver/decision/$', view="driver_decision"),

	url(r'^save/device/$',view="save_device"),
	url(r'^send/gcm/$',view="send_gcm"),

	url(r'^alltest/$',view="get_all_test"),
	url(r'^request/client/$',view="request_from_client"),
	url(r'^companies/$',view="get_companies",name="companies"),
	url(r'^create/user/$',view="create_super_user",name="user"),
	url(r'^edit/$',view="edit_company_view",name="edit_company"),
	url(r'^$',view="company_view",name="company"),
)