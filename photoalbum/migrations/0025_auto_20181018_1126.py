# Generated by Django 2.1 on 2018-10-18 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0024_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='Komentarz'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='photoalbum.Photo',
                verbose_name='Zdjęcie'
            ),
        ),
    ]
