# Generated by Django 2.1 on 2018-10-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0026_auto_20181018_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='photo',
            new_name='picture',
        ),
    ]
