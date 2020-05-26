from os import path



from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone


from mdeditor.fields import MDTextField



from saintexupery.utils import unique_slug_generator_identif, upload_file_location






# Create your models here.


class Presentation(models.Model):

    titre           = models.CharField(max_length=255, default="Présentation des cycles du centre")
    slug            = models.SlugField()
    image           = models.FileField(upload_to=upload_file_location)
    description     = MDTextField()

    created         = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)






    def __str__(self):
        return self.titre


    class Meta:
        verbose_name = "Présention des cycles"
        verbose_name_plural ="Présentations des cycles"


def presentation_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_identif(instance, instance.titre)



pre_save.connect(presentation_pre_save_receiver, sender=Presentation)







class Cycle(models.Model):

    PRIMAIRE = "primaire"
    COLLEGE = "college"
    LYCEE = "lycee"


    CYCLES = (
                (PRIMAIRE,"primaire"),
                (COLLEGE, "Collège"),
                (LYCEE, "Lycée")
        )
    nom             = models.CharField(max_length=255)
    niveau_cycle    = models.CharField(max_length=255, choices=CYCLES)
    classes         = models.CharField(max_length=255)
    slug            = models.SlugField()

    image           = models.FileField(upload_to=upload_file_location)
    description     = MDTextField()

    created         = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)





    def __str__(self):
        return self.niveau_cycle


    class Meta:
        ordering = ["-created", "-updated"]
        verbose_name = "Cycle"
        verbose_name_plural ="Les cycles"



def cycle_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_identif(instance, instance.nom)



pre_save.connect(cycle_pre_save_receiver, sender=Cycle)


