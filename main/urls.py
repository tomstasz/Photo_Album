"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path
from photoalbum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.AddUserView.as_view(), name='register'),
    path('add_photo', views.PhotoUploadView.as_view(), name='add_photo'),
    path('delete_photo/<pk>',
         views.PhotoDeleteView.as_view(),
         name='delete_photo'),
    path('photo_detail/<pk>',
         views.PhotoDetailView.as_view(),
         name='photo_detail'),
    path('my_profile', views.MyProfileView.as_view(), name='profile'),
    path('update_photo/<pk>',
         views.PhotoUpdateView.as_view(),
         name='update_photo'),
    path('reset_password/<id>',
         views.ResetPasswordView.as_view(),
         name='reset_password'),
    path('delete_user/<pk>',
         views.UserDeleteView.as_view(),
         name='delete_user'),
    path('like_photo', views.like_photo, name='like_photo'),
    path('delete_comment/<pk>',
         views.CommentDeleteView.as_view(),
         name='delete_comment'),
    path('update_comment/<pk>',
         views.CommentUpdateView.as_view(),
         name='update_comment'),
] + staticfiles_urlpatterns() + \
  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
