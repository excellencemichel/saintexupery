from django import forms
from mdeditor.fields import MDTextFormField


from saintexupery.utils import unique_slug_generator_identif

from .models import Cycle, Presention


class CycleForm(forms.ModelForm):
	nom 				= forms.CharField(label="nom du cycle")
	description 		= MDTextFormField(label="La description du cyle")

	class Meta:
		model = Cycle
		exclude = ["slug"]


	def save(self, commit=True):
		instance = super(CycleForm, self).save(commit=False)

		if not instance.slug:
			instance.slug = unique_slug_generator_identif(instance, instance.nom)
		if commit:
			instance.save()
		
		return instance




class PresentionForm(forms.ModelForm):
	titre 			= forms.CharField(label="Titre")
	description 	= MDTextFormField(label="Description globale des cyles")

	class Meta:
		model = Presention
		exclude = ["slug"]


	def save(self, commit=True):
		instance = super(PresentionForm, self).save(commit=False)

		if not instance.slug:
			instance.slug = unique_slug_generator_identif(instance, instance.titre)
		if commit:
			instance.save()
		
		return instance