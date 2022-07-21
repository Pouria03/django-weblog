from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import *


# sign up user using django system
class UserRegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request,'you are logged in', 'success')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account created successfully . login please', 'success')
            return redirect('login')
        return render(request, 'account/register.html', {'form': form})


# login user using django system

class UserLoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request,'you are logged in', 'success')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username']
                                , password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you are logged in now! enjoy', 'success')
                return redirect('post:posts')
            else:
                messages.warning(request, 'invalid information', 'warning')
        return render(request, 'account/login.html', {'form': form})


#  logout user
class UserLogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you have logged out', 'success')
        return redirect('home:home')
