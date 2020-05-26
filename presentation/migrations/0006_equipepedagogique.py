# Generated by Django 2.0.3 on 2020-05-25 03:32

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0005_partenaire_lien_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipePedagogique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('presentation', mdeditor.fields.MDTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]