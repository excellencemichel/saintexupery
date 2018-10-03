from django.shortcuts import render

# Create your views here.



def presentation_cycles(request):
	context = {}

	return render(request, "cycles/presentation_cycles.html", context)


def primaire(request):

    context = {}

    return render(request, "cycles/primaire.html", context)



def college(request):

    context = {}

    return  render(request, "cycles/college.html", context)


def lycee(request):

    context = {}

    return  render(request, "cycles/lycee.html", context)
