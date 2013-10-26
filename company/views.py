# Create your views here.
from company.models import Company
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def company_view(request):
	company, created = Company.objects.get_or_create(user=request.user)	
	ctx = {'company':company}
	return render_to_response('company/company.html',ctx,context_instance=RequestContext(request))