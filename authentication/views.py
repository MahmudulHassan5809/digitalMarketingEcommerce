from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import Profile
from .forms import UserForm
from django.views import View


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        ProfileInlineFormset = inlineformset_factory(User, Profile, fields=(
            'profile_pic', 'phone_number', 'address'), extra=1, can_delete=False)
        formset = ProfileInlineFormset()
        return render(request, 'authentication/register.html', {
            "noodle_form": user_form,
            "formset": formset,
            "login_form" : False
        })

    def post(self, request, *args, **kwargs):
        phone_number = request.POST.get('user_profile-0-phone_number')
        address = request.POST.get('user_profile-0-address')
        profile_pic = request.FILES.get('user_profile-0-profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username == '' or address == '' or first_name == '' or last_name == '' or email == '' or password == '':
            messages.error(request, 'Please Input All The Fields')
            return redirect('auth:register')
        else:
            valid_user = User.objects.filter(username=username).first()

            if valid_user:
                messages.error(request, 'Username already taken')
                return redirect('auth:register')

            valid_user = User.objects.filter(email=email).first()

            if valid_user:
                messages.error(request, 'Email already taken')
                return redirect('auth:register')

            created_user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)

            profile = get_object_or_404(Profile, user=created_user)
            profile.profile_pic = profile_pic
            profile.phone_number = phone_number
            profile.address = address
            profile.save()

            messages.success(
                request, 'You are now registered and can login now')

            return redirect('auth:register')



class LoginView(View):
    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        ProfileInlineFormset = inlineformset_factory(User, Profile, fields=(
            'profile_pic', 'phone_number', 'address'), extra=1, can_delete=False)
        formset = ProfileInlineFormset()
        return render(request, 'authentication/register.html', {
            "noodle_form": user_form,
            "formset": formset,
            "login_from" : True
        })
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if username == '' or password == '':
            messages.error(request, ('Please Input All The Field'))
            return redirect('auth:login')
        elif user is not None:
            login(request, user)
            return redirect('store:home')
        else:
            messages.error(request, ('Invalid Credentials'))
            return redirect('auth:login')