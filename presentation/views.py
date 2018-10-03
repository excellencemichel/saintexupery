from django.shortcuts import render

# Create your views here.



def presentation(request):


	context = {}
	return render(request, "presentation/presentation.html", context)



def partenaires(request):

	context = {}

	return render(request, "presentation/partenaire.html", context)



def mot_directeur(request):
	context = {}

	return render(request, "presentation/mot_directeur.html", context)


def programme(request):

	context = {}

	return render(request, "presentation/programme.html", context)



def equipe_pedagogique(request):
	context = {}

	return render(request, "presentation/equipe_pedagogique.html", context)

