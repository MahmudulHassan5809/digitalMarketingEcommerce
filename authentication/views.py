from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm
from django.views import View


class RegisterView(View):
	def get(self, request, *args, **kwargs):
		user_form = UserForm()
		ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('profile_pic', 'phone_number', 'address'),extra=1, can_delete=False)
		formset = ProfileInlineFormset()
		return render(request,'authentication/register.html',{
			"noodle_form" : user_form,
			"formset": formset
		})
        