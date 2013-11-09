from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('company.views',

	url(r'^companies/$',view="get_companies",name="companies"),
	url(r'^create/user/$',view="create_super_user",name="user"),
	url(r'^edit/$',view="edit_company_view",name="edit_company"),
	url(r'^$',view="company_view",name="company"),
)