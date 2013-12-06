from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from gcm.models import Device
from client.models import Client
from django.http import HttpResponseRedirect, HttpResponse

@csrf_exempt
def save_client(request):
	device_reg = request.POST['device_reg']
	name = request.POST['name']
	phone = request.POST['phone']

	my_phone = Device.objects.get(dev_id=device_reg)

	cl, created = Client.objects.get_or_create(name=name,number=phone,device=my_phone)
	return HttpResponse("SAVED") 
