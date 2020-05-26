from django.contrib import admin


from .models import Candidature
# Register your models here.


@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
	list_filter = ("civilite", "poste", "created") #Pour les champs qui vont s'afficher dans l'admin
