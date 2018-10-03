
from django.utils.translation import ugettext_lazy as _
from re import match



from django import forms


#local
from .models import Inscription





FREQUENCE = (
			("premiere","1ère inscription"),
			("renouvellment", "Renouvellement")
	)

SEXE = (
			("masculin", "Masculin"),
			("feminin", "Féminin"),
		)


REPRESENTANT_PARENT_UN = (
				("pere", "Père"),
				("personne_morale", "Personne morale "),
			)


REPRESENTANT_PARENT_DEUX = (
				("mere", "Mère"),
				("personne_morale", "Personne morale "),
			)

SITUATION_FAMILIALE = (
				("marie", "Marié"),
				("vie_mariale_ou_PACS", "Vie Mariale ou PACS"),
				("divorce_ou_separe", "Divorcé(e) ou séparé(e)"),
				("celibataire", "Célibataire"),
				("veuf", "Veuf(ve)"),
	)


NIVEAU = (
			("maternelle", "Maternelle"),
			("cp1", "1ère Année ou CP1"),
			("cp2", "2ème Année ou CP2"),
			("ce1", "3ème Année ou CE1"),
			("ce2", "4ème Année ou CE2"),
			("cm1", "5ème Année ou CM1"),
			("cm2", "1ère Année ou CM2"),
			("sixieme", "Classe de 6ème"),
			("cinquième", "Classe de 5ème"),
			("quatrieme", "Classe de 4ème"),
			("troisiem", "Classe de 3ème"),

			("deuxieme", "Classe de 2ème"),
			("premiere", "class de 1ère lycée"),
			("terminale", "Classe de terminale"),


	)






class InscriptionModelForm(forms.ModelForm):

	niveau 									= forms.ChoiceField(choices=NIVEAU, required=True
																)

	frequence 								= forms.ChoiceField(

														widget=forms.RadioSelect, choices=FREQUENCE, required=True
														)



	sexe 									= forms.ChoiceField(widget=forms.RadioSelect, choices=SEXE, required=True
													)




	#############################"""""""""""" Représentant parent 1 #########################################""

	representant_parent_un 					= forms.ChoiceField(widget=forms.RadioSelect, choices=REPRESENTANT_PARENT_UN, required=True)



	#############################"""""""""""" Représentant parent 2 #########################################""


	representant_parent_deux 				= forms.ChoiceField(widget=forms.RadioSelect, choices=REPRESENTANT_PARENT_DEUX, required=True)




	################################""""""""" Situation Familiale """"""""""""####################
	situation_familiale 					= forms.ChoiceField( label = _("Situation familiale"),
																	widget=forms.RadioSelect, choices=SITUATION_FAMILIALE, required=True)


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
						"placeholder":"Loua",
					}
			),

						"prenom": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Michel",
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
						"placeholder":"",
					}
			),



						"nationalite": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... Française",
					}
			),



						"telephone": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 06 33 77 12 40",
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
						"placeholder":"Dupond",
					}
			),


						"prenom_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Patrice",
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
						"placeholder":"",
					}
			),


						"code_postal_naissance_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"",
					}
			),


						"nationalite_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"",
					}
			),


						"adresse_domicile_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"",
					}
			),


						"ville_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"",
					}
			),



						"telephone_domicile_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 06 33 77 12 40",
					}
			),


						"telephone_personnel_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 06 33 77 12 40",
					}
			),


						"telephone_professionnel_parent_un": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 06 33 77 12 40",
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
						"placeholder":"Ex... Entrepreneur...",
					}
			),

			
				##############"""" Info Parent 2 """""########
						"nom_jeune_fille_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"",
					}
			),

					
						"nom_marial_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... Cathérine...",
					}
			),

					
						"prenom_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... Cathérine...",
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
						"placeholder":"",
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
						"placeholder":"",
					}
			),

					
						"telephone_domicile_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 06 33 77 12 40",
					}
			),

					
						"telephone_personnel_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 06 33 77 12 40",
					}
			),

		
						"telephone_professionnel_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"Ex... 06 33 77 12 40",
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
						"placeholder":"Ex... Entrepreneur...",
					}
			),

					
						"adresse_domicile_parent_deux": forms.TextInput(
					attrs = {
						"class": "form-control input-sm",
						"placeholder":"",
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
