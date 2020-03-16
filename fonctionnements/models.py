from django.db import models

# Create your models here.


class Infobule(models.Model):
    info = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
