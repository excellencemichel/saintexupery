from django.shortcuts import render

# Create your views here.


def fonctionnement(request):
	context = {}

	return render(request, "fonctionnements/fonctionnement_.html", context)

def horaires(request):

    context = {}

    return  render(request, "fonctionnements/horaires_.html", context)


def vacances(request):

    context = {}

    return  render(request, "fonctionnements/vacances_.html")
