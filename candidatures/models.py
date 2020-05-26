from django.db import models
from saintexupery.utils import upload_file_location

# Create your models here.

class Candidature(models.Model):
	MR = "Mr"
	MME = "Mme"
	MELLE = "Melle"

	CIVILITE = (
		(MR, "Mr"),
		(MME, "Mme"),
		(MELLE, "Melle")
		)

	nom 			= models.CharField(max_length=250)
	prenom 			= models.CharField(max_length=250)
	civilite 		= models.CharField( max_length=250,choices=CIVILITE)
	email 			= models.EmailField()
	telephone 		= models.CharField(max_length=33)
	cv 				= models.FileField(upload_to=upload_file_location)
	poste 			= models.CharField(max_length=250)
	message 		= models.TextField()
	created         = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated         = models.DateTimeField(auto_now=True, auto_now_add=False)

	class Meta:
		verbose_name = "La Candidature"
		verbose_name_plural = "Les Candidatures"




	def __str__(self):
		return "Candidature de {nom} {prenom}".format(nom=self.nom, prenom =self.prenom)

