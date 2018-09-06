from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView
from photoalbum.forms import LoginForm, AddUserForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from .models import User


class IndexView(View):

    def get(self, request):
        return TemplateResponse(request, 'photoalbum/index.html', {'message': 'Witaj świecie'})


class LoginView(View):

    def get(self, request):
        return TemplateResponse(request, 'photoalbum/login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        ctx = {'form': form, 'message': None}
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                ctx.update({'message': 'Błąd loginu lub hasła'})
        return TemplateResponse(request, 'photoalbum/login.html', ctx)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class AddUserView(View):

    def get(self, request):
        form = AddUserForm()
        return TemplateResponse(request, 'photoalbum/user_form.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            email = form.cleaned_data['login']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=email, email=email, password=password)
            login(request, new_user)
            return redirect('index')
        return TemplateResponse(request, 'photoalbum/user_form.html', ctx)

