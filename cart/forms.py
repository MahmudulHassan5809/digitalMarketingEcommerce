from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm



class CheckOutForm(forms.Form):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email =  forms.EmailField(required=True)
	address = forms.CharField()
	country = forms.CharField(required=True)
	state = forms.CharField(required=True)
	zip_code =  forms.CharField(required=True)