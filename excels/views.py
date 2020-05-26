from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required

import django_excel as excel



#local import 
from ._compact import JsonResponse
from inscriptions.models import Inscription

# Create your views here.


@login_required
def exports_data(request):
	context = {}

	return render(request, "excels/exports_data.html", context)

@login_required
def export_inscription_data(request, atype):
	if atype == "sheet":
		return excel.make_response_from_a_table(

			Inscription, "xlsx", file_name="inscriptions"
			)
	elif atype =="custom":
		query_sets = Inscription.objects.all()
		column_names = ["nom", "prenom", "date_inscription", "date_naissance", "lieu_naissance", 
		"niveau", "frequence", "sexe", "nationalite", "telephone", "email", 
		"representant_parent_un", "nom_parent_un", "prenom_parent_un", 
		"date_naissance_parent_un", "lieu_naissance_parent_un", 
		"code_postal_naissance_parent_un", "nationalite_parent_un",
		"adresse_domicile_parent_un", "ville_parent_un", "telephone_domicile_parent_un", 
		"telephone_personnel_parent_un", "telephone_professionnel_parent_un", "email_parent_un",
		"profession_parent_un",

		"representant_parent_deux", "nom_jeune_fille_parent_deux", "nom_marial_parent_deux", "prenom_parent_deux", 
		"date_naissance_parent_deux", "lieu_naissance_parent_deux", "code_postal_naissance_parent_deux", 
		"nationalite_parent_deux", "telephone_domicile_parent_deux", "telephone_personnel_parent_deux",
		 "telephone_professionnel_parent_deux", "email_parent_deux", "profession_parent_deux",
		"adresse_domicile_parent_deux","situation_familiale", "matricule"

	]
		return excel.make_response_from_query_sets(

				query_sets,
				column_names,
				"xlsx",
				file_name="inscriptions"
			)
	else:
		return HttpResponseBadRequest(
			"Bad request. S'il vous plait mettez l'un des choses dans le suffix de votre URL : sheet ou custom "
			)



@login_required
def embed_handson_inscription_table(request):
    """
    Renders one table in a handsontable
    """
    fields_exclude = ('id', "pdf_inscription", "image_enfant", )
    content = excel.pe.save_as(
        model=Inscription,
        exclude = fields_exclude,
        dest_file_type='handsontable.html',
        dest_embed=True)
    content.seek(0)
    return render(
        request,
        'custom-handson-table.html',
        {
            'handsontable_content': content.read()
        })