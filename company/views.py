# Create your views here.
from company.models import Company
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from company.forms import editCompanyForm
from django.views.generic.create_update import create_object, delete_object,update_object
from cabbie.models import Driver, Car
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import sys
from django.http import HttpResponseRedirect, HttpResponse

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
