from django.shortcuts import render

from activites.models import Activite
from evenements.models import Article

# Create your views here.



def home(request):

	instance_activites = Activite.objects.all()[:5]
	instance_articles= Article.objects.all()[:5]
	
	context = {
		"instance_activites": instance_activites,

		"instance_evenements" : instance_articles,
	}
	return render(request, "home.html", context)




def navs(request):

	context = {}

	return render(request, "navs.html", context)