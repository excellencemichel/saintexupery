from django.shortcuts import render, get_object_or_404


from .models import Presentation, Cycle

# Create your views here.



def presentation(request):
	instance = Presentation.objects.first()
	cycles = Cycle.objects.all()
	primaire = cycles.filter(niveau_cycle=Cycle.PRIMAIRE)
	college = cycles.filter(niveau_cycle=Cycle.COLLEGE)
	lycee = cycles.filter(niveau_cycle = Cycle.LYCEE)
	context = {
		"instance" : instance,
		"primaire": primaire,
		"college": college,
		"lycee" : lycee
	}

	return render(request, "cycles/presentation.html", context)





def primaire(request):
	instance = Cycle.objects.filter(niveau_cycle=Cycle.PRIMAIRE).first()

	context = {
    	"instance": instance
    	}

	return render(request, "cycles/primaire.html", context)



def college(request):
	instance = Cycle.objects.filter(niveau_cycle=Cycle.COLLEGE).first()

	context = {
    	"instance": instance
    	}

	return  render(request, "cycles/college.html", context)


def lycee(request):
	instance = Cycle.objects.filter(niveau_cycle=Cycle.LYCEE).first()
	context = {
    	"instance": instance
    }

	return  render(request, "cycles/lycee.html", context)
