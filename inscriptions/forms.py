
from datetime import date

from django.utils.translation import ugettext_lazy as _
from re import match

from captcha.fields import CaptchaField



from django import forms


#local
from .models import Inscription











class InscriptionModelForm(forms.ModelForm):

	date_naissance 		= forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year-23, date.today().year)))

	niveau 									= forms.ChoiceField(choices=Inscription.NIVEAU, required=True
																)

	frequence 								= forms.ChoiceField(

														widget=forms.RadioSelect, choices=Inscription.FREQUENCE, required=True
														)



	sexe 									= forms.ChoiceField(widget=forms.RadioSelect, choices=Inscription.SEXE, required=True
													)




	#############################"""""""""""" Représentant parent 1 #########################################""

	representant_parent_un 					= forms.ChoiceField(widget=forms.RadioSelect, choices=Inscription.REPRESENTANT_PARENT_UN, required=True)
	date_naissance_parent_un 				= forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year-85, date.today().year)))




	#############################"""""""""""" Représentant parent 2 #########################################""


	representant_parent_deux 				= forms.ChoiceField(widget=forms.RadioSelect, choices=Inscription.REPRESENTANT_PARENT_DEUX, required=True)
	date_naissance_parent_deux 				= forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year-85, date.today().year)))





	################################""""""""" Situation Familiale """"""""""""####################
	situation_familiale 					= forms.ChoiceField( label = _("Situation familiale"),
																	widget=forms.RadioSelect, choices=Inscription.SITUATION_FAMILIALE, required=True)

	captcha = CaptchaField()



	class Meta:
		model = Inscription
		exclude = ['pdf_inscription', 'matricule']


		labels = {

			#########""" Info Elève """"""#########""
            "nom": _("Nom"),
            "prenom": _("Prénom"),
            "date_naissance" : _("Date de naissance"),
            "lieu_naissance": _("Lieu de naissance"),
            "niveau" : _("Niveau"),
            "frequence": _("Est-ce : "),
            "sexe": _("SEXE"),
            "nationalite" : _("Nationalité"),
            "telephone" : _("Téléphone"),
            "email": _("Adresse email"),


            ########""""""""" Info Parent 1"""""##########
            "nom_parent_un": _("Nom"),
            "prenom_parent_un": _("Prénom"),
            "date_naissance_parent_un": "Date de naissance",
            "lieu_naissance_parent_un" : "Lieu de naissance",
            "code_postal_naissance_parent_un" : "Code postal de naissance",
            "nationalite_parent_un": "Nationalité",
            "adresse_domicile_parent_un": "Adresse du domicile",
            "ville_parent_un": "Ville de résidence",
            "telephone_domicile_parent_un": "Téléphone de domicile",
            "telephone_personnel_parent_un": "Téléphone personnel",
            "telephone_professionnel_parent_un" : "Téléphone professionnel",
            "email_parent_un": "Email",
            "profession_parent_un": "Profession",

            ##########"""""""" Info Parent 1 """""""""#########
            "nom_jeune_fille_parent_deux" : "Nom de jeune fille si ça existe",
            "nom_marial_parent_deux": "Nom Marial",
            "prenom_parent_deux" : "Prénom",
            "date_naissance_parent_deux": "Date de naissance",
            "lieu_naissance_parent_deux" : "Lieu de naissance",
            "code_postal_naissance_parent_deux": "Code postal",
            "nationalite_parent_deux" : "Nationalité",
            "telephone_domicile_parent_deux": "Téléphone de domicile",
            "telephone_personnel_parent_deux" :"Téléphone personnel",
            "telephone_professionnel_parent_deux" : "Téléphone professionnel",
            "email_parent_deux" : "Email",
            "profession_parent_deux" : "Adresse de domicile",


            ##########""""""""""" Situation Familiale """"""####################
            "situation_familiale" : "Situation familiale",





       		 }


        
		widgets = {
			
			"nom": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

						"prenom": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),



						"date_naissance": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 12/12/2003",
					}
			),


						"lieu_naissance": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),



						"nationalite": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),



						"telephone": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"+212...",
					}
			),


						"email": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"example@gmail.com",
					}
			),

			#########""""""" Info Parent 1 """""###########

						"nom_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),


						"prenom_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),


						"date_naissance_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"12/12/1977",
					}
			),

						"lieu_naissance_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
					
					}
			),


						"code_postal_naissance_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
				
					}
			),


						"nationalite_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),


						"adresse_domicile_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),


						"ville_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),



						"telephone_domicile_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"+212...",
					}
			),


						"telephone_personnel_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"+212...",
					}
			),


						"telephone_professionnel_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"+212..",
					}
			),


						"email_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"example@gmail.com",
					}
			),


		
						"profession_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

			
				##############"""" Info Parent 2 """""########
						"nom_jeune_fille_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

					
						"nom_marial_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

					
						"prenom_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

					
						"date_naissance_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex 12/12/1977",
					}
			),

					
						"lieu_naissance_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

					
						"code_postal_naissance_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"",
					}
			),

					
						"nationalite_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
					
					}
			),

					
						"telephone_domicile_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"+212...",
					}
			),

					
						"telephone_personnel_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"+212...",
					}
			),

		
						"telephone_professionnel_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"+212",
					}
			),

					
						"email_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"example@gmail.com",
					}
			),

					
						"profession_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

					
						"adresse_domicile_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						
					}
			),

			
						



		 }













	def clean_telephone(self):
		telephone = self.cleaned_data["telephone"]

		# controle = r"^6[2-9][0-9]([ .-]?[0-9]{2}){3}$" #Pour la Guinée
		controle = r"^0[5-7]([-. ]?[0-9]{2}){4}$" #Pour le Maroc


		if match(controle, telephone):
			return telephone
		else:
			raise forms.ValidationError(_("Votre numéro de téléphone ne correspond pas à un numéro de téléphone marocain"))



	def clean_telephone_domicile_prent_un(self):
		telephone_domicile_parent_un = self.cleaned_data["telephone_domicile_parent_un"]

		controle = r"^0[5-7]([-. ]?[0-9]{2}){4}$" #Pour le Maroc
		

		if match(controle, telephone_domicile_parent_un):
			return telephone_domicile_parent_un
		else:
			raise forms.ValidationError(_("Votre numéro de téléphone ne correspond pas à un numéro de téléphone marocain"))



	def clean_personnel_parent_un(self):
		telephone_personnel_parent_un = self.cleaned_data["telephone_personnel_parent_un"]
		controle = r"^0[5-7]([-. ]?[0-9]{2}){4}$" #Pour le Maroc


		if match(controle, telephone_personnel_parent_un):
			return telephone_personnel_parent_un
		else:
			raise forms.ValidationError(_("Votre numéro de téléphone ne correspond pas à un numéro de téléphone marocain"))



	def clean_professionnel_parent_un(self):
		telephone_professionnel_parent_un = self.cleaned_data["telephone_professionnel_parent_un"]
		controle = r"^0[5-7]([-. ]?[0-9]{2}){4}$" #Pour le Maroc
		

		if match(controle, telephone_professionnel_parent_un):
			return telephone_professionnel_parent_un
		else:
			raise forms.ValidationError(_("Votre numéro de téléphone ne correspond pas à un numéro de téléphone marocain"))


	def clean_domicile_parent_deux(self):
		telephone_domicile_parent_deux = self.cleaned_data["telephone_domicile_parent_deux"]
		controle = r"^0[5-7]([-. ]?[0-9]{2}){4}$" #Pour le Maroc


		if match(controle, telephone_domicile_parent_deux):
			return telephone_domicile_parent_deux
		else:
			raise forms.ValidationError(_("Votre numéro de téléphone ne correspond pas à un numéro de téléphone marocain"))



	def clean_personnel_parent_deux(self):
		telephone_personnel_parent_un = self.cleaned_data["telephone_personnel_parent_un"]
		controle = r"^0[5-7]([-. ]?[0-9]{2}){4}$" #Pour le Maroc

		

		if match(controle, telephone_personnel_parent_un):
			return telephone_personnel_parent_un
		else:
			raise forms.ValidationError(_("Votre numéro de téléphone ne correspond pas à un numéro de téléphone marocain"))



	def clean_professionnel_parent_deux(self):
		telephone_professionnel_parent_deux = self.cleaned_data["telephone_professionnel_parent_deux"]
		controle = r"^0[5-7]([-. ]?[0-9]{2}){4}$" #Pour le Maroc

		if match(controle, telephone_professionnel_parent_deux):
			return telephone_professionnel_parent_deux
		else:
			raise forms.ValidationError(_("Votre numéro de téléphone ne correspond pas à un numéro de téléphone marocain"))
