from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('company.views',

	url(r'^edit/$',view="edit_company_view",name="edit_company"),
	url(r'^$',view="company_view",name="company"),
)