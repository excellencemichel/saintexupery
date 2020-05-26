from django import forms
from mdeditor.fields import MDTextFormField


from saintexupery.utils import unique_slug_generator_identif

from .models import Partenaire, Generale






class PartenaireForm(forms.ModelForm):
	nom 			= forms.CharField(label="Infobule")
	lien_site   	= forms.URLField(label="Lien de son site ou page")
	contenu 		= MDTextFormField(label="Le contenu")

	class Meta:
		model = Partenaire
		exclude = ["slug"]


	def save(self, commit=True):
		instance = super(PartenaireForm, self).save(commit=False)
		print("Voici instance", instance)

		if not instance.slug:
			instance.slug = unique_slug_generator_identif(instance, instance.nom)
		if commit:
			instance.save()
		
		return instance
