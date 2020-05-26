from django.shortcuts import render, get_object_or_404

from .models import Infobule, Calendrier, Horaire




# Create your views here.


def horaires(request):
    instance = Horaire.objects.all().last()
    print("Le titre l'instance est >:", instance.titre)

    context = {
        "instance" : instance,
    }

    return  render(request, "fonctionnements/horaires.html", context)


def calendrier_scolaire(request):
    instance = Calendrier.objects.last()
    print("Le titre de l'instance est >:", instance.titre)

    context = {
        "instance" : instance,
    }

    return  render(request, "fonctionnements/calendrier_scolaire.html", context)


def infobules(request):
    instances = Infobule.objects.all()

    context = {
        "instances": instances,
    }

    return render(request, "fonctionnements/infobules.html", context)


def infobule(request, id=None, slug=None):
    instance = get_object_or_404(Infobule, id=id, slug=slug)

    context = {
        "instance": instance,
    }

    return render(request, "fonctionnements/infobule.html", context)

