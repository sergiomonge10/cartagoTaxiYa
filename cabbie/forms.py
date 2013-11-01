from django import forms
from cabbie.models import Driver,Car

class editDriverForm(forms.ModelForm):    
    class Meta:
        model = Driver
        exclude = ('object_id','company')

class editCarForm(forms.ModelForm):    
    class Meta:
        model = Car
        exclude = ('object_id')