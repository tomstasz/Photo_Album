from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from photoalbum.forms import LoginForm, AddUserForm, PhotoUploadForm, PhotoUpdateForm, ResetPasswordForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from .models import User, Photo


class IndexView(View):

    def get(self, request):
        all_photo = Photo.objects.order_by('creation_date')
        return TemplateResponse(request, 'photoalbum/index.html', {'photos': all_photo})


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


class PhotoUploadView(View):
    template_name = 'photoalbum/photo_form.html'

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        form = PhotoUploadForm(initial={'user': user})
        return TemplateResponse(request, self.template_name, {'form': form})

    def post(self, request):
        form = PhotoUploadForm(request.POST, request.FILES)
        ctx = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('index')
        return TemplateResponse(request, self.template_name, ctx)


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('profile')


class PhotoDetailView(View):

    def get(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        ctx = {'photo': photo}
        return TemplateResponse(request, 'photoalbum/photo_detail.html', ctx)


class MyProfileView(View):

    def get(self, request):
        User = request.user
        photos = User.photo_set.all()
        return TemplateResponse(request, 'photoalbum/profile.html', {'photos': photos})


class PhotoUpdateView(View):

    def get(self, request, pk):
        photo = Photo.objects.get(id=pk)
        form = PhotoUpdateForm(instance=photo)
        return TemplateResponse(request, 'photoalbum/photo_update.html', {'form': form, 'photo': photo})

    def post(self, request, pk):
        photo = Photo.objects.get(id=pk)
        form = PhotoUpdateForm(request.POST, request.FILES, instance=photo)
        ctx = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('profile')
        return TemplateResponse(request, 'photoalbum/photo_update.html', ctx)


class ResetPasswordView(PermissionRequiredMixin, View):
    permission_required = 'auth.change_user'

    def get(self, request, id):
        form = ResetPasswordForm()
        user = User.objects.get(id=id)
        return TemplateResponse(request, 'photoalbum/reset_password.html', {'form': form, 'user': user})

    def post(self, request, id):
        form = ResetPasswordForm(request.POST)
        user = User.objects.get(id=id)
        ctx = {'form': form, 'user': user}
        if form.is_valid():
            new_pass = form.cleaned_data['new_pass']
            user.set_password(new_pass)
            user.save()
            logout(request)
            ctx.update({'message': "Hasło zostało zmienione, zaloguj się ponownie."})

        else:
            ctx.update({'message': 'Błędne dane w formularzu'})
        return TemplateResponse(request, 'photoalbum/reset_password.html', ctx)