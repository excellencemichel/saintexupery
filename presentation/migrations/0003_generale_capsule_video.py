# Generated by Django 2.0.3 on 2020-05-23 04:11

from django.db import migrations, models
import presentation.models
import saintexupery.utils


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0002_generale_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='generale',
            name='capsule_video',
            field=models.FileField(blank=True, null=True, upload_to=saintexupery.utils.upload_file_location),
        ),
    ]
