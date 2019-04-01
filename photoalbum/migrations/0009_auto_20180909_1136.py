# Generated by Django 2.1 on 2018-09-09 11:36

from django.db import migrations, models
import easy_thumbnails.fields
import photoalbum.models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0008_auto_20180909_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(
                blank=True,
                max_length=128,
                null=True,
                upload_to=photoalbum.models.user_directory,
                verbose_name='Zdjęcie'
            ),
        ),
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=models.ImageField(
                max_length=128,
                upload_to=photoalbum.models.user_directory,
                verbose_name='Zdjęcie'
            ),
        ),
    ]
