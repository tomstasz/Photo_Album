from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView
from photoalbum.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from photoalbum.models import User


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
                ctx.update({'message': 'Nie ma takiego użytkownika'})
        return TemplateResponse(request, 'photoalbum/login.html', ctx)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class UserCreateView(CreateView):
    model = User
    # fields = ['username', 'password', 'first_name', 'last_name', 'email']
    fields = '__all__'
    template_name = 'photoalbum/user_form.html'
    success_url = reverse_lazy('index')
