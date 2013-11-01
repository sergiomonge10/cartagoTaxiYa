from django import forms
from company.models import Company

class editCompanyForm(forms.ModelForm):    
    class Meta:
        model = Company
        exclude = ('object_id', 'user')