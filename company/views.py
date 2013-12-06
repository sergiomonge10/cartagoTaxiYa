# Create your views here.
from company.models import Company, Location,Prueba
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from company.forms import editCompanyForm
from django.views.generic.create_update import create_object, delete_object,update_object
from cabbie.models import Driver, Car, Driver_Decision
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import sys
from django.http import HttpResponseRedirect, HttpResponse
from cabbie.models import DriverLocation, Driver
from gcm.models import Device
import time
from client.models import Client
from django.core.exceptions import ObjectDoesNotExist

@login_required
def company_view(request):
    company, created = Company.objects.get_or_create(user=request.user)
    driver = Driver.objects.filter(company=company)
    ctx = {'company':company,'driver':driver}
    return render_to_response('company/company.html',ctx, context_instance=RequestContext(request))

@login_required
def edit_company_view(request):
	company = Company.objects.get(user=request.user)
	return update_object(request,
        form_class=editCompanyForm,
        object_id = company.id,
        template_name = 'company/edit_company.html',
        extra_context = {'company':company},
        post_save_redirect = "/company",
    )

def create_super_user(request):
    # TODO: Don't actually use this bogus admin account.
    default_username = 'admin'
    default_pass = '1234'
    default_email = 'sergiomonge10@gmail.com'
    if authenticate(username=default_username, password=default_pass) is not None:
        return HttpResponse("User already created.")
    try:
        user = User.objects.create_user(default_username, default_email, default_pass)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return HttpResponse("User created!")
    except:
        print sys.exc_info()[0]
        return HttpResponse("Couldnt create user.")

from django.core import serializers
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

def get_companies(request):
    # get the objects you wish to return
    companies = Company.objects.all()
    # construct a list which will contain all of the data for the response
    to_json = []
    for c in companies:
        # for each object, construct a dictionary containing the data you wish to return
        cm_dict = {}
        cm_dict['name'] = c.name
        cm_dict['phone'] = c.phone
        # ...etc
        # append the dictionary of each dog to the list
        to_json.append(cm_dict)
    #create json
    list_companies = {}
    list_companies['Companies'] = to_json
    # convert the list to JSON
    response_data = simplejson.dumps(list_companies)
    # return an HttpResponse with the JSON and the correct MIME type
    return HttpResponse(response_data, mimetype='application/json')


@csrf_exempt
def request_from_client(request):

    lat = request.POST['latitude']
    lon = request.POST['longitude']
    coun = request.POST['country']
    city = request.POST['city']
    dev_id = request.POST['dev_id']

    location = Location()
    location.lat = lat
    location.lon = lon
    location.country = coun
    location.city = city
    location.save()
    
    if send_notification_to_driver(city=city,lat=lat,lon=lon,client_dev_id=dev_id):
        return HttpResponse("OKAY")
    else:
        return HttpResponse("NO :(")


def send_notification_to_driver(city,lat,lon,client_dev_id):

    current_city = city

    driver_location = DriverLocation.objects.filter(city=current_city)

    client_device = Device.objects.get(dev_id=client_dev_id)
    client = Client.objects.get(device=client_device)

    for d in driver_location:
        device_id = d.driver.device.dev_id
        driver_nid = d.driver.nid
        if d.driver.device.is_active:
            send_gcm(device_id=device_id,lat=lat,lon=lon,nid=driver_nid)

            #AQUI VALIDAR LA DESCICION DEL MAE
            
            #driver = Driver.objects.get(nid=driver_nid)
            #driver_decision = Driver_Decision.objects.get(driver=d.driver)

            exist = False
            while exist == False:
                try:
                    driver_decision = Driver_Decision.objects.get(driver=d.driver)
                    exist = True
                except ObjectDoesNotExist:
                    exist = False

            driver_decision = Driver_Decision.objects.get(driver=d.driver)

            if driver_decision.decision :
                # Send a message to client
                #time.sleep(10)
                client_device.send_message_to_client(msg="El taxi ya va hacia su destino")

                p = Prueba()
                p.description = "Sirvio el mae de" + d.city
                p.save()

                #Driver_Decision.objects.get(driver=d.driver).delete()

                return True

@csrf_exempt
def driver_decision(request):
    driver_nid = request.POST['nid']
    decision = request.POST['decision']
    driver = Driver.objects.get(nid=driver_nid)
    decision_bool = False

    if decision == 'true':
        decision_bool = True
    else:
        decision_bool = False

    d = Driver_Decision()
    d.driver = driver
    d.decision = decision_bool
    d.save()

    return HttpResponse('SAVED DECISION')

@csrf_exempt
def save_device(request):
    device_id = request.POST['device_id']
    driver = request.POST['driver_nid']
    my_phone = Device.objects.get(reg_id=device_id)

    driver = Driver.objects.get(nid=driver)
    driver.device = my_phone
    driver.save()

    return HttpResponse("SAVED") 

def send_gcm(device_id,lat,lon,nid):
    my_phone = Device.objects.get(dev_id=device_id)
    my_phone.send_message('Desea recoger este cliente ?',lat,lon,nid)

def get_all_test(request):
    loc = Location.objects.all()
    ctx = {'loc':loc}
    return render_to_response('all_test.html',ctx,context_instance=RequestContext(request))

def prueba_gcm(request):
    my_phone = Device.objects.get(dev_id="5db8dd140141a18e")
    my_phone.send_message('El taxi se dirige a su destino',0,0,0)
    return HttpResponse("SENDED")