from django.shortcuts import render

from .models import Generale,  Partenaire 

# Create your views here.



def presentation(request):
	instance = Generale.objects.filter(presentation_type=Generale.PRESENTATION).first()

	context = {
	"instance": instance
	}
	return render(request, "presentation/presentation.html", context)






def mot_directeur(request):
	instance = Generale.objects.filter(presentation_type=Generale.MOT_DIRECTEUR).first()

	context = {
	"instance":instance
	}

	return render(request, "presentation/mot_directeur.html", context)


def programme(request):
	instance = Generale.objects.filter(presentation_type=Generale.PROGRAMME).first()

	context = {
	"instance": instance
	}

	return render(request, "presentation/programme.html", context)



def equipe_pedagogique(request):
	instance = Generale.objects.filter(presentation_type=Generale.EQUIPE_PEDAGOGIQUE).first()

	context = {
	"instance": instance
	}

	return render(request, "presentation/equipe_pedagogique.html", context)

def partenaires(request):
	instances = Partenaire.objects.all()

	context = {
	"instances":instances
	}

	return render(request, "presentation/partenaire.html", context)
