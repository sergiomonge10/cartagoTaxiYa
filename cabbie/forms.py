from django import forms
from cabbie.models import Driver,Car
from django import forms

class editDriverForm(forms.ModelForm):    
    class Meta:
    	password = forms.CharField(widget=forms.PasswordInput)
        model = Driver
        widgets = {
            'password': forms.PasswordInput(),
        }
        exclude = ('object_id','company','device')

class editCarForm(forms.ModelForm):    
    class Meta:
        model = Car
        exclude = ('object_id')