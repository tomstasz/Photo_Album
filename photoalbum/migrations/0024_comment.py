# Generated by Django 2.1 on 2018-10-18 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoalbum', '0023_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('photo', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='photoalbum.Photo'
                )),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Użytkownik'
                )),
            ],
        ),
    ]
