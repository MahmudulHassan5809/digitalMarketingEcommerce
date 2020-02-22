from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from authentication.models import Profile

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email','password')

	
		

