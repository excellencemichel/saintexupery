from django.core.mail import EmailMultiAlternatives


from django.utils.translation import pgettext, ugettext, ugettext_lazy as _

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template import loader
from django.template.loader import get_template



from django import forms

from captcha.fields import CaptchaField

from .models import Candidature 




class CandidatureForm(forms.ModelForm):

	nom 			= forms.CharField(label="Votre nom", widget=forms.TextInput(
					attrs = {
						"class": "form-control input-xs",
					}), required=True)

	prenom 			= forms.CharField(label="Votre prénom", widget=forms.TextInput(
					attrs = {
						"class": "form-control input-xs",
					}), required=True)
	# civilite 		= forms.ChoiceField( label = _("Civilité"),widget=forms.RadioSelect, choices=Candidature.CIVILITE, required=True)

	email 			= forms.EmailField(label="Votre mail", widget=forms.TextInput(
					attrs = {
						"class": "form-control input-xs",
					}), required=True)

	cv 				= forms.FileField(label="Votre CV", required=True)
	poste 			= forms.CharField(label="Pour quel poste postulez-vous ?",widget=forms.TextInput(
					attrs = {
						"class": "form-control input-xs",
					}), required=True)

	message = forms.CharField(label=_("Message à laisser"),
		widget=forms.Textarea(attrs={"class": "form-control input-lg", "placeholder": "Message: limité à 5000 caractères"}),
		)

	captcha = CaptchaField()

	class Meta:
		model = Candidature
		fields = ["nom", "prenom", "email", "cv", "poste", "message"]


	def clean_message(self):
	    # Check that the two password entries match
	    message = self.cleaned_data.get("message")
	    message_reel = message.strip()
	    mots = message_reel.split(" ")
	    if len(mots) > 5000:
	        raise forms.ValidationError(_("Votre message ne doit pas depasser 5000 mots"))
	    return message
