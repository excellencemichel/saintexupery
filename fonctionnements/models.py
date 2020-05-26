from django.db import models
from django.db.models.signals import pre_save

from django.urls import reverse

from mdeditor.fields import MDTextField

from saintexupery.utils import unique_slug_generator_for_null, upload_file_location



# Create your models here.


class Infobule(models.Model):
    """
    Class pour afficher les dernières nouvells
    """
	slug 			= models.SlugField(max_length=1000, blank=True )
	info 			= models.CharField(max_length=1000)
	contenu 		= MDTextField()
	created 		= models.DateTimeField(auto_now=False, auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.info

	def get_absolute_url(self):
		return reverse("fonctionnements:infobule", kwargs={"id": self.id, "slug": self.slug})

	class Meta:
		ordering = ["-created", "-updated"]



def infob_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator_for_null(instance)



pre_save.connect(infob_pre_save_receiver, sender=Infobule)





######################### Cheldle################






class Calendrier(models.Model):
    titre           = models.CharField(max_length=255, default="Calendrier scolaire")
    description     = MDTextField()
    doc_pdf 		= models.FileField(upload_to=upload_file_location, null=True, blank=True)

    created         = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)






    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Calendrier scolaire"
        verbose_name_plural ="Calendriers scolaire"






class Horaire(models.Model):

    titre           = models.CharField(max_length=255, default="Horaire")
    description     = MDTextField()
    doc_pdf 		= models.FileField(upload_to=upload_file_location, null=True, blank=True)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)






    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("cycles:detail", kwargs={"id": self.id, "slug": self.slug})


    class Meta:
        verbose_name = "Horaire"
        verbose_name_plural ="Horaires"

