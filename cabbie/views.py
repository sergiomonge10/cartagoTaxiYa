from cabbie.models import Driver, Car, TypeCar
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from cabbie.forms import editDriverForm, editCarForm
from django.views.generic.create_update import create_object, delete_object,update_object
from company.models import Company

@login_required
def add_driver_view(request):
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        name = ""
        nid = ""
        description = ""
        price = ""
        stock = ""
        form = editDriverForm(request.POST)
        info = "Inicializando"

        if form.is_valid():
            nid = form.cleaned_data['nid']
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            enable = form.cleaned_data['enable']
 
            d = Driver()
            d.nid = nid
            d.name = name
            d.lastname = lastname
            d.phone = phone
            d.enable = enable
            d.company = company
            d.save()
            info = "Se guardo satisfactoriamente, puedes agregar otro"
        else:
            info =  "ERROR: Asegurese que los datos sean correctos."
        form = editDriverForm()
        contexto = {'form': form, 'info': info,'company':company}
        return render_to_response('cabbie/add_driver.html', contexto, context_instance=RequestContext(request))
    else:
        form = editDriverForm()
        contexto = {'form': form, 'company':company}
        return render_to_response('cabbie/add_driver.html', contexto, context_instance=RequestContext(request))

@login_required
def edit_driver_view(request):
	driver = Driver.objects.get(user=request.user)
	return update_object(request,
        form_class=editDriverForm,
        object_id = driver.id,
        template_name = 'cabbie/edit_driver.html',
        extra_context = {'driver':driver},
        post_save_redirect = "/company",
	)

@login_required
def edit_Car_view(request):
	Car = Car.objects.get(user=request.user)
	return update_object(request,
        form_class=editCarForm,
        object_id = car.id,
        template_name = 'cabbie/edit_car.html',
        extra_context = {'car':car},
        post_save_redirect = "/company",
	)