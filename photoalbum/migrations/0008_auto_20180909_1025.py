# Generated by Django 2.1 on 2018-09-09 10:25

from django.db import migrations
import easy_thumbnails.fields
import photoalbum.models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0007_auto_20180907_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=easy_thumbnails.fields.ThumbnailerImageField(
                max_length=128,
                upload_to=photoalbum.models.user_directory,
                verbose_name='Zdjęcie'
            ),
        ),
    ]
