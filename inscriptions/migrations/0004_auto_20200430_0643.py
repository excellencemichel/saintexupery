# Generated by Django 2.0.3 on 2020-04-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0003_auto_20200430_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='date_naissance',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_naissance_parent_un',
            field=models.CharField(max_length=250),
        ),
    ]