from django.shortcuts import render

# Create your views here.



def presentation_cycles(request):
	context = {}

	return render(request, "cycles/pres.html", context)



def primaire(request):

    context = {}

    return render(request, "cycles/primaire_.html", context)



def college(request):

    context = {}

    return  render(request, "cycles/college_.html", context)


def lycee(request):

    context = {}

    return  render(request, "cycles/lycee_.html", context)
