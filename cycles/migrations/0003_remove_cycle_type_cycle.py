# Generated by Django 2.0.3 on 2020-05-23 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycles', '0002_auto_20200523_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycle',
            name='type_cycle',
        ),
    ]