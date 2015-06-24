import datetime

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import utc
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserCreationForm, LoginForm

from django.contrib.auth import authenticate, login, logout

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/login_user/')
    else:
        form = UserCreationForm()
    return render(request, 'task/createuser.html', {'form': form})

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
    else:
        form = LoginForm()
    return render(request, 'task/loginuser.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/account/login_user/')