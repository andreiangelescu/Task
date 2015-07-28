
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import utc
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.context_processors import csrf
from forms import *
from models import *
from django.template import RequestContext

from .forms import UserCreationForm, LoginForm, ActivationForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout

import hashlib, datetime, random
from django.utils import timezone

def create_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            form.save()

            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
            activation_key = hashlib.sha1(salt+email).hexdigest()            
            #key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by email
            user = MyUser.objects.get(email=email)
            user.activation_key = activation_key
            user.save()

            #Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. Your activation key is:%s To activate your account, click this link http://127.0.0.1:8000/account/account_verification/ or click the following link to auto-activate it http://127.0.0.1:8000/account/account_verification/%s" % (email, activation_key, activation_key)

            send_mail(email_subject, email_body, 'activarecont23@gmail.com',[email], fail_silently=False)

            return render(request, 'task/ActivationRedirect.html')
    else:
        form = UserCreationForm()
    return render(request, 'task/createuser.html', {'form': form})

class RegisterConfirm2Ways(FormView):
    form_class = ActivationForm
    template_name = 'task/ActivationKey.html'
    template_name_complete = 'task/ActivationComplete.html'
    success_url = reverse_lazy('account_manager:activation_complete')

    def get(self, request, *args, **kwargs):
        if "activation_key" in kwargs.keys():
            self.activation_key = kwargs.get('activation_key')
        return super(RegisterConfirm2Ways, self).get(request, *args, **kwargs)
    
    def get_template_names(self):
        if hasattr(self, 'activation_key'):
            form = self.form_class({'activation_field':self.activation_key})
            if form.is_valid():
                return self.template_name_complete
            else:
                raise forms.ValidationError('Activation key incorect!')
        return super(RegisterConfirm2Ways, self).get_template_names()

    # def get_context_data(self, **kwargs):
    #     kwargs = super(RegisterConfirm2Ways, self).get_context_data(**kwargs)
    #     if self.get_key_errors:
    #         kwargs.update({'get_key_errors':self.get_key_errors})
    #     return kwargs

class ActivationComplete(TemplateView):
    template_name = 'task/ActivationComplete.html'

def login_user(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/task/tasks/')
            else:
                form = LoginForm()
            return render(request, 'task/loginuserTEXT.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'task/loginuser.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'task/logoutTEXT.html')

    #Activation click on link or manual with a form

    # def register_confirm(request):
#     form = ActivationForm()
#     if request.method == 'POST':
#         form = ActivationForm(request.POST)
#         if form.is_valid():
#             user = None
#             activation_field = form.cleaned_data['activation_field']
#             if MyUser.objects.filter(activation_key=activation_field).exists():
#                 user = MyUser.objects.get(activation_key=activation_field)
#             if user and activation_field == user.activation_key:
#                 user.is_active = True
#                 user.save()
#             else:
#                 return render(request, 'task/ActivationKeyIncorect.html', {'form':form})

#             return render(request, 'task/ActivationComplete.html')
#     else:
#         return render(request, 'task/ActivationKey.html', {'form':form})

# def register_confirm_auto(request, activation_key):
#     user = None
#     if MyUser.objects.filter(activation_key=activation_key).exists():
#         user = MyUser.objects.get(activation_key=activation_key)
#     if user and activation_key == user.activation_key:
#         user.is_active = True
#         user.save()
#     else:
#         return render(request, 'task/AutoActivationKeyInvalid.html')
    
#     return render(request, 'task/ActivationComplete.html')