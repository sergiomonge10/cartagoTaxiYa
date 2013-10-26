from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *

urlpatterns = patterns('company.views',

		url(r'^',view="company_view",name="company"),

    )