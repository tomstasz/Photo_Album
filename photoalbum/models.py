from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


def user_directory(instance, filename):
    return 'user_{}/{}'.format(instance.user.id, filename)


class Photo(models.Model):
    path = models.ImageField(upload_to=user_directory, max_length=128, verbose_name='Zdjęcie')
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")



