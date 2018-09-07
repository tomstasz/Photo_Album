# Generated by Django 2.1 on 2018-09-07 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0003_auto_20180907_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=models.ImageField(max_length=128, upload_to='images', verbose_name='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
    ]
