from django.shortcuts import render

# Create your views here.


def horaires(request):

    context = {}

    return  render(request, "fonctionnements/horaires.html", context)


def calendrier_scolaire(request):

    context = {}

    return  render(request, "fonctionnements/calendrier_scolaire.html")
