from django.db import models

# Create your models here.

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




class Inscription(models.Model):

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

	date_naissance_parent_un 			= models.CharField(max_length=250)

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

	date_naissance_parent_deux 			= models.CharField(max_length=250)
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







