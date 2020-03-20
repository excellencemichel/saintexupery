from  django.utils import timezone
from django.urls import reverse


from django.db import models

# Create your models here.





class Contact(models.Model):

	nom = models.CharField(max_length=250)
	prenom = models.CharField(max_length=250)
	telephone = models.CharField(max_length=250)
	email = models.EmailField()

	subject = models.CharField(max_length=250)

	message = models.TextField()

	created = models.DateTimeField(default = timezone.now)



	def __str__(self):

		return str(self.nom)



	def get_absolute_url(self):


		name_url = "contacts:detail"

		return reverse(name_url, kwargs={"id":self.id })
