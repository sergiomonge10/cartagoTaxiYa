from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from cabbie.models import Driver, Car, TypeCar, Route
from taxiya.views import contact_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	model = User

class GroupViewSet(viewsets.ModelViewSet):
	model = Group

class DriverViewSet(viewsets.ModelViewSet):
	model = Driver

class CarViewSet(viewsets.ModelViewSet):
	model = Car

class TypeCarViewSet(viewsets.ModelViewSet):
	model = TypeCar

class RouterViewSet(viewsets.ModelViewSet):
	model = Route

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'cars', CarViewSet)
router.register(r'typecars', TypeCarViewSet)
router.register(r'routers', RouterViewSet)


urlpatterns = patterns('',
   
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^cabbie/', include('cabbie.urls')),
    url(r'^company/', include('company.urls')),

    url(r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
    #url(r'', include('gcm.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^contact/$', view=contact_view, name="contact"),

    url(r'^', include('gcm.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^api/', include(router.urls)),
	url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += staticfiles_urlpatterns()
