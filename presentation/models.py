from os import path

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save

from mdeditor.fields import MDTextField


from saintexupery.utils import unique_slug_generator, unique_slug_generator_identif, upload_file_location




# Create your models here.


class Generale(models.Model):
    PRESENTATION = "presentation"
    MOT_DIRECTEUR = "mot_directrice"
    EQUIPE_PEDAGOGIQUE = "equipe_pedagogique"
    PROGRAMME = "programme"

    TYPE_PRESENTATION = (

        (PRESENTATION, "Présentation"),
        (MOT_DIRECTEUR, "Mot du directeur"),
        (PROGRAMME, "Programe du CNED"),
        (EQUIPE_PEDAGOGIQUE, "Equipe pédagogique"),

        )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


    content = MDTextField()
    image = models.FileField(upload_to=upload_file_location, null=True, blank=True)
    capsule_video = models.FileField(upload_to=upload_file_location, null=True, blank=True)
    presentation_type = models.CharField(max_length=250, choices=TYPE_PRESENTATION)


    created = models.DateTimeField(auto_now=False, auto_now_add=True)


    updated = models.DateTimeField(auto_now=True, auto_now_add=False)




    def __str__(self):
        if self.presentation_type == self.PRESENTATION:
            return "Présentation"
        elif self.presentation_type == self.MOT_DIRECTEUR:
            return "Mot de la direction"
        elif self.presentation_type == self.EQUIPE_PEDAGOGIQUE:
            return "Équipe pédagogique"

        elif self.presentation_type == self.PROGRAMME:
            return "Programme"


    class Meta:
    	verbose_name = "Le centre"
    	verbose_name_plural = "Le centre"





class Partenaire(models.Model):
    nom         = models.CharField(max_length=250)
    slug        = models.SlugField()
    logo        = models.ImageField(upload_to=upload_file_location, null=True, blank=True)
    lien_site   = models.URLField(max_length=1000, null=True, blank=True)
    contenu     = MDTextField()
    created     = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)



    def __str__(self):
        return "Partenaire {nom}".format(nom=self.nom)








def partenaire_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_identif(instance, instance.nom)



pre_save.connect(partenaire_pre_save_receiver, sender=Partenaire)

