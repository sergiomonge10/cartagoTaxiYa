from django import forms


class ContactForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Title = forms.CharField(widget=forms.TextInput())
	Comment = forms.CharField(widget=forms.Textarea())