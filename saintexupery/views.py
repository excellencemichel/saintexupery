from django.shortcuts import render

from evenements.models import Article
from presentation.models import  Partenaire, Generale


# Create your views here.



def home(request):

	instance_articles= Article.objects.all()[:5]
	partenaires = Partenaire.objects.all()[:7]
	presentation = Generale.objects.filter(presentation_type=Generale.PRESENTATION).first()
	
	context = {

		"instance_evenements" : instance_articles,
		"partenaires":partenaires,
		"presentation": presentation,
	}
	return render(request, "home.html", context)




def navs(request):

	context = {}

	return render(request, "navs.html", context)