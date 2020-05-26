from django import forms
from django.db import models


from mdeditor.fields import MDTextFormField


from saintexupery.utils import unique_slug_generator_for_null

from .models import Infobule, Calendrier,Horaire





class InfobuleForm(forms.ModelForm):
	info 			= forms.CharField(label="Infobule")
	contenu 		= MDTextFormField(label="Le contenu")

	class Meta:
		model = Infobule
		exclude = ["slug"]


	def save(self, commit=True):
		instance = super(InfobuleForm, self).save(commit=False)
		print("Voici instance", instance)

		if not instance.slug:
			instance.slug = unique_slug_generator_for_null(instance)
		if commit:
			instance.save()
		
		return instance




class CalendrierForm(forms.ModelForm):
    # titre           = forms.CharField(label="Titre")
    description     = MDTextFormField(label="le Calendrier")

    class Meta:
    	model = Calendrier
    	fields = "__all__"



class HoraireForm(forms.ModelForm):
    # titre           = forms.CharField(label="Titre")
    description     = MDTextFormField(label="Les horaires")

    class Meta:
    	model = Horaire
    	fields= "__all__"