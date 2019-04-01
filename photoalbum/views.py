import json

from django.contrib.auth.mixins import (PermissionRequiredMixin,
                                        LoginRequiredMixin)
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy, reverse
from .models import User, Photo, Like, Comment
from django.forms.models import modelform_factory
from django import forms

from photoalbum.forms import (LoginForm,
                              AddUserForm,
                              PhotoUploadForm,
                              PhotoUpdateForm,
                              ResetPasswordForm,
                              AddCommentForm)


class IndexView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        all_photo = Photo.objects.order_by('creation_date')
        likes = Like.objects.filter(user=request.user)
        likes_list = list()
        for like in likes:
            likes_list.append(like.photo_id)
        ctx = {'photos': all_photo,
               'likes': likes_list,
               }
        return TemplateResponse(request, 'photoalbum/index.html', ctx)


class LoginView(View):

    def get(self, request):
        return TemplateResponse(request,
                                'photoalbum/login.html',
                                {'form': LoginForm()})

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
        return TemplateResponse(request,
                                'photoalbum/user_form.html',
                                {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            email = form.cleaned_data['login']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=email,
                                                email=email,
                                                password=password)
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


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.delete_user'
    model = User
    template_name = 'photoalbum/user_confirm_delete.html'
    success_url = reverse_lazy('index')


class PhotoDetailView(View):

    def get(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        comments = photo.comment_set.order_by('date')
        form = AddCommentForm()
        ctx = {'form': form,
               'photo': photo,
               'comments': comments}
        return TemplateResponse(request, 'photoalbum/photo_detail.html', ctx)

    def post(self, request, pk):
        form = AddCommentForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            comment = form.cleaned_data['content']
            Comment.objects.create(content=comment,
                                   user=request.user,
                                   photo_id=pk)
            return redirect('photo_detail', pk=pk)
        return TemplateResponse(request, 'photoalbum/photo_detail.html', ctx)


class MyProfileView(View):

    def get(self, request):
        user = request.user
        photos = user.photo_set.all()
        return TemplateResponse(request,
                                'photoalbum/profile.html',
                                {'photos': photos})


class PhotoUpdateView(View):

    def get(self, request, pk):
        photo = Photo.objects.get(id=pk)
        form = PhotoUpdateForm(instance=photo)
        return TemplateResponse(request,
                                'photoalbum/photo_update.html',
                                {'form': form, 'photo': photo})

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
        return TemplateResponse(request,
                                'photoalbum/reset_password.html',
                                {'form': form, 'user': user})

    def post(self, request, id):
        form = ResetPasswordForm(request.POST)
        user = User.objects.get(id=id)
        ctx = {'form': form, 'user': user}
        if form.is_valid():
            new_pass = form.cleaned_data['new_pass']
            user.set_password(new_pass)
            user.save()
            logout(request)
            ctx.update({'message': """
            Hasło zostało zmienione, zaloguj się ponownie.
            """
                        })
        else:
            ctx.update({'message': 'Błędne dane w formularzu'})
        return TemplateResponse(request, 'photoalbum/reset_password.html', ctx)


def like_photo(request):
    if request.method == 'POST':
        photo_id = request.POST['photo_id']
        is_liked = request.POST['is_liked']
        liked_photo = Photo.objects.get(id=photo_id)
        if is_liked == 'true':
            like = Like.objects.filter(photo=liked_photo, user=request.user)[0]
            like.delete()
        else:
            Like.objects.create(photo=liked_photo, user=request.user)
        count_likes = Like.objects.filter(photo_id=photo_id)
        count_likes = len(count_likes)
        to_dump = dict()
        to_dump['count_likes'] = count_likes

        return HttpResponse(json.dumps(to_dump))
    return HttpResponse("Invalid method")


class CommentDeleteView(DeleteView):
    model = Comment
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('photo_detail')

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.photo.id})


class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model,
                                 fields=self.fields,
                                 widgets=self.widgets)


class CommentUpdateView(ModelFormWidgetMixin, UpdateView):
    model = Comment
    fields = ['content']
    widgets = {'content': forms.Textarea(attrs={'cols': 40, 'rows': 3})}
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('photo_detail')

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.photo.id})
