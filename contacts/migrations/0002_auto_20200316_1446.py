# Generated by Django 2.0.3 on 2020-03-16 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='profession',
            new_name='telephone',
        ),
    ]
