# Generated by Django 2.0.3 on 2020-04-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0005_auto_20200430_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='date_naissance',
            field=models.CharField(max_length=250),
        ),
    ]