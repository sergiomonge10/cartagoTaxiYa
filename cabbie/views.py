from cabbie.models import Driver, Car, TypeCar
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from cabbie.forms import editDriverForm, editCarForm
from django.views.generic.create_update import create_object, delete_object,update_object
from company.models import Company
from django.http import HttpResponse, HttpResponseBadRequest


@login_required
def add_driver_view(request):
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        name = ""
        nid = ""
        password = ""
        lastname = ""
        phone = ""
        car = ""

        form = editDriverForm(request.POST)
        info = "Inicializando"
        info_send = False

        if form.is_valid():
            nid = form.cleaned_data['nid']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            enable = form.cleaned_data['enable']
            car = form.cleaned_data['car']
 
            d = Driver()
            d.nid = nid
            d.name = name
            d.lastname = lastname
            d.phone = phone
            d.enable = enable
            d.company = company
            d.password = password
            d.save()

            for c in car.all():
                d.car.add(c)
                
            info = "Se guardo satisfactoriamente, puedes agregar otro"
            info_send = True
        else:
            info =  "ERROR: Asegurese que los datos sean correctos."
        form = editDriverForm()
        contexto = {'form': form, 'info': info,'info_send':info_send,'company':company}
        return render_to_response('cabbie/add_driver.html', contexto, context_instance=RequestContext(request))
    else:
        form = editDriverForm()
        contexto = {'form': form, 'company':company}
        return render_to_response('cabbie/add_driver.html', contexto, context_instance=RequestContext(request))

@login_required
def add_car_view(request):
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        number = ""
        type_car = ""
        reader_card = ""
        form = editCarForm(request.POST)
        info = "Inicializando"
        info_send = False

        if form.is_valid():
            number = form.cleaned_data['number']
            type_car = form.cleaned_data['type_car']
            reader_card = form.cleaned_data['reader_card']
 
            c = Car()
            c.number = number
            c.type_car = type_car
            c.reader_card = reader_card
            c.save()
            info = "Se guardo satisfactoriamente, puedes agregar otro"
            info_send = True
        else:
            info =  "ERROR: Asegurese que los datos sean correctos."
        form = editCarForm()
        contexto = {'form': form, 'info': info,'info_send':info_send,'company':company}
        return render_to_response('cabbie/add_car.html', contexto, context_instance=RequestContext(request))
    else:
        form = editCarForm()
        contexto = {'form': form, 'company':company}
        return render_to_response('cabbie/add_car.html', contexto, context_instance=RequestContext(request))



@login_required
def edit_driver_view(request,nid):
    company = Company.objects.get(user=request.user)
    driver = Driver.objects.filter(company=company).get(nid=nid)
    return update_object(request,
        form_class=editDriverForm,
        object_id = driver.id,
        template_name = 'cabbie/edit_driver.html',
        extra_context = {'driver':driver, 'company':company},
        post_save_redirect = "/company",
	)

@login_required
def edit_car_view(request,number):
    company = Company.objects.get(user=request.user)
    car = Car.objects.get(number=number)
    return update_object(request,
        form_class=editCarForm,
        object_id = car.id,
        template_name = 'cabbie/edit_car.html',
        extra_context = {'car':car, 'company':company},
        post_save_redirect = "/company",
	)

"""
@login_required
def delete_driver_view(request,nid):
    driver = Driver.objects.get(nid=nid)
    return delete_object(request,
        model=Driver,
        object_id=driver.id,
        post_delete_redirect="/company",)
"""

@login_required
def delete_driver_view(request,nid):
    Driver.objects.get(nid=nid).delete()
    return HttpResponse("DELETED")


from django.core import serializers
from django.utils import simplejson

def get_drivers(request):
    # get the objects you wish to return
    driver = Driver.objects.all()
    # construct a list which will contain all of the data for the response
    to_json = []
    for d in driver:
        # for each object, construct a dictionary containing the data you wish to return
        dr_dict = {}
        dr_dict['nid'] = d.nid
        dr_dict['password'] = d.password
        # ...etc
        # append the dictionary of each dog to the list
        to_json.append(dr_dict)
    # convert the list to JSON
    response_data = simplejson.dumps(to_json)
    # return an HttpResponse with the JSON and the correct MIME type
    return HttpResponse(response_data, mimetype='application/json')

def get_types(request):
    # get the objects you wish to return
    types = TypeCar.objects.all()
    # construct a list which will contain all of the data for the response
    to_json = []
    for t in types:
        # for each object, construct a dictionary containing the data you wish to return
        ty_dict = {}
        ty_dict['name'] = t.name
        # ...etc
        # append the dictionary of each dog to the list
        to_json.append(ty_dict)
    #create json
    list_types = {}
    list_types['Types'] = to_json
    # convert the list to JSON
    response_data = simplejson.dumps(list_types)
    # return an HttpResponse with the JSON and the correct MIME type
    return HttpResponse(response_data, mimetype='application/json')

#def receive_request_from_client(request,position):

