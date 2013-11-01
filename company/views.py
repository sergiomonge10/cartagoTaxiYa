# Create your views here.
from company.models import Company
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from company.forms import editCompanyForm
from django.views.generic.create_update import create_object, delete_object,update_object
from cabbie.models import Driver

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