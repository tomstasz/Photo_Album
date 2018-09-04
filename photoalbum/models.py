from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Photo(models.Model):
    path = models.CharField(max_length=64, verbose_name='ścieżka')
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

