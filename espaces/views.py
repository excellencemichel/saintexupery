from django.shortcuts import render

# Create your views here.




def espace_etudiant(request):

	context = {}


	return render(request, "espaces/espace_etudiant.html", context)