# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from taxiya.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.views.generic.create_update import create_object, delete_object,update_object

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import sys

def contact_view(request):
	info_send = False #define si se envia la informacion
	email = ""
	title = ""
	comment = ""
	if request.method == 'POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_send = True
			email = formulario.cleaned_data['Email']
			title = formulario.cleaned_data['Title']
			comment = formulario.cleaned_data['Comment']

			#Configuracion enviando mensaje via GMAIL
			to_admin = 'sergiomonge10@gmail.com'
			html_content = "Informacion Recibida de [%s] <br><br><br>***Mensaje***<br><br>%s"%(email,comment)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = ContactForm()

	ctx = {'form':formulario,'email':email,'title':title,'comment':comment,'info_send':info_send}
	return render_to_response('taxiya/contact.html',ctx,context_instance=RequestContext(request))
