# Generated by Django 2.1 on 2018-09-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=models.ImageField(max_length=128, upload_to='images', verbose_name='ścieżka'),
        ),
    ]
