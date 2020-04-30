from django.db import models

# Create your models here.



class Inscription(models.Model):

	FREQUENCE_PREMIERE = "premiere"
	FREQUENCE_RENOUVELLEMENT = "renouvellment"

	FREQUENCE = (
				(FREQUENCE_PREMIERE,"1ère inscription"),
				(FREQUENCE_RENOUVELLEMENT, "Renouvellement")
		)

	SEXE_MASCULIN = "masculin"
	SEXE_FEMININ = "feminin"
	SEXE = (
				(SEXE_MASCULIN, "Masculin"),
				(SEXE_FEMININ, "Féminin"),
			)


	REPRESENTANT_PARENT_UN_PERE = "pere"
	REPRESENTANT_PARENT_UN_MERE = "mere"

	REPRESENTANT_PARENT_UN = (
					(REPRESENTANT_PARENT_UN_PERE, "Père"),
					(REPRESENTANT_PARENT_UN_MERE, "Personne morale "),
				)

	REPRESENTANT_PARENT_DEUX_PERE = "pere"
	REPRESENTANT_PARENT_DEUX_MERE = "mere"

	REPRESENTANT_PARENT_DEUX = (
					(REPRESENTANT_PARENT_DEUX_PERE, "Mère"),
					(REPRESENTANT_PARENT_DEUX_MERE, "Personne morale "),
				)



	SITUATION_FAMILIALE_MARIE = "marie"
	SITUATION_FAMILIALE_VIE_MARIALE_OU_PACS = "vie_mariale_ou_PACS"
	SITUATION_FAMILIALE_DIVORCE_OU_SEPARE = "divorce_ou_separe"
	SITUATION_FAMILIALE_CELIBATAIRE = "celibataire"
	SITUATION_FAMILIALE_VEUF = "veuf"

	SITUATION_FAMILIALE = (
					(SITUATION_FAMILIALE_MARIE, "Marié"),
					(SITUATION_FAMILIALE_VIE_MARIALE_OU_PACS, "Vie Mariale ou PACS"),
					(SITUATION_FAMILIALE_DIVORCE_OU_SEPARE, "Divorcé(e) ou séparé(e)"),
					(SITUATION_FAMILIALE_CELIBATAIRE, "Célibataire"),
					(SITUATION_FAMILIALE_VEUF, "Veuf(ve)"),
		)



	NIVEAU_CE1 = "ce1"
	NIVEAU_CE2 = "ce2"
	NIVEAU_CE3 = "ce3"
	NIVEAU_CE4 = "ce4"
	NIVEAU_CE5 = "ce5"
	NIVEAU_CE6 = "ce6"
	NIVEAU_CE7 = "ce7"
	NIVEAU_CE8 = "ce8"
	NIVEAU_CE9 = "ce9"
	NIVEAU_DEUXIEME = "deuxieme"
	NIVEAU_PREMIERE_GENERALE = "premiere_generale"
	NIVEAU_PREMIERE_STMG = "premiere_stmg"
	NIVEAU_TERMINALE_GENERALE = "terminale_generale"
	NIVEAU_TERMINALE_STMG = "terminale_stmg"


	NIVEAU = (
		("Grande section maternelle primaire", ( 
				(NIVEAU_CE1, "CP ou CE1"),
				(NIVEAU_CE2, "CE1  ou CE2"),
				(NIVEAU_CE3, "CE2  ou CE3"),
				(NIVEAU_CE4, "CM1 ou CE4"),
				(NIVEAU_CE5, "CM2 ou CE5"),
				)),

		("Collège", ( 

				(NIVEAU_CE6, "6ème ou CE6"),
				(NIVEAU_CE7, "5ème ou CE7"),
				(NIVEAU_CE8, "4ème CE8"),
				(NIVEAU_CE9, "3ème ou CE9"),

				)),
		("Lycée", (

				(NIVEAU_DEUXIEME, "2de ou tronc commun"),
				(NIVEAU_PREMIERE_GENERALE, "1ère générale ou 1ère lycée"),
				(NIVEAU_PREMIERE_STMG, "1ère STMG ou 2ème année lycée"),
				(NIVEAU_TERMINALE_GENERALE, "Terminale Générale"),
				(NIVEAU_TERMINALE_STMG, "Terminale STMG")


				))
		)


	nom 				= models.CharField(max_length=250)

	prenom 				= models.CharField(max_length=250)
	date_naissance 		= models.DateField()
	lieu_naissance 		= models.CharField(max_length=250)

	niveau 				= models.CharField(max_length=250, choices=NIVEAU)

	frequence 			= models.CharField(max_length=250, choices=FREQUENCE)



	sexe 				= models.CharField(max_length=250, choices=SEXE)


	nationalite 		= models.CharField(max_length=250)

	telephone 			= models.CharField(max_length=250)

	email 				= models.EmailField()


	#############################"""""""""""" Représentant parent 1 #########################################""

	representant_parent_un 				= models.CharField(max_length=250, choices=REPRESENTANT_PARENT_UN)

	nom_parent_un 						= models.CharField(max_length=250)

	prenom_parent_un 					= models.CharField(max_length=250)

	date_naissance_parent_un 			= models.DateField()

	lieu_naissance_parent_un			= models.CharField(max_length=250)

	code_postal_naissance_parent_un 	= models.CharField(max_length=250)
	nationalite_parent_un				= models.CharField(max_length=250)
	adresse_domicile_parent_un			= models.CharField(max_length=250)

	ville_parent_un						= models.CharField(max_length=250)

	telephone_domicile_parent_un 		= models.CharField(max_length=250)
	telephone_personnel_parent_un 		= models.CharField(max_length=250)

	telephone_professionnel_parent_un 	= models.CharField(max_length=250)

	email_parent_un 					= models.EmailField()
	profession_parent_un 				= models.CharField(max_length=250)




	#############################"""""""""""" Représentant parent 2 #########################################""


	representant_parent_deux 			= models.CharField(max_length=250, choices=REPRESENTANT_PARENT_DEUX)
	nom_jeune_fille_parent_deux			= models.CharField(max_length=250, null=True, blank=True)
	nom_marial_parent_deux 				= models.CharField(max_length=250)

	prenom_parent_deux 					= models.CharField(max_length=250)

	date_naissance_parent_deux 			= models.DateField()
	lieu_naissance_parent_deux			= models.CharField(max_length=250)

	code_postal_naissance_parent_deux 	= models.CharField(max_length=250)
	nationalite_parent_deux				= models.CharField(max_length=250)

	telephone_domicile_parent_deux 		= models.CharField(max_length=250)
	telephone_personnel_parent_deux 	= models.CharField(max_length=250)

	telephone_professionnel_parent_deux = models.CharField(max_length=250)

	email_parent_deux 					= models.EmailField()
	profession_parent_deux 				= models.CharField(max_length=250)
	adresse_domicile_parent_deux			= models.CharField(max_length=250, null=True, blank=True)


	################################""""""""" Situation matrimoniale """"""""""""####################
	situation_familiale 				= models.CharField(max_length=250, null=True, choices=SITUATION_FAMILIALE)

	##############################""""""" Entrée du pdf """"""""""""""""""""""#####################


	pdf_inscription		= models.FileField(upload_to="pdfs", null=True, blank=True)
	matricule 							= models.CharField(max_length=255)
	image_enfant		= models.ImageField(null=True, blank=True)


	def __str__(self):
		return str(self.nom)







