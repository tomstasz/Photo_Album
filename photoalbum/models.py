from django.db import models
from django.contrib.auth import get_user_model
# from easy_thumbnails.alias import aliases
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

saved_file.connect(generate_aliases_global)

# Create your models here.

# if not aliases.get('photoalbum'):
#     aliases.set('photoalbum', {'size': (500, 250), 'crop': True})

User = get_user_model()


def user_directory(instance, filename):
    return 'user_{}/{}'.format(instance.user.id, filename)


class Photo(models.Model):
    title = models.CharField(max_length=64,
                             verbose_name='Tytuł',
                             null=True,
                             blank=True)
    path = models.ImageField(upload_to=user_directory, verbose_name='Zdjęcie')
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Użytkownik")


class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=500, verbose_name="Komentarz")
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Użytkownik")
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photo,
                              on_delete=models.CASCADE,
                              verbose_name="Zdjęcie")
