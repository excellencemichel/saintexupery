from django.contrib import admin
from .models import Activite, ActiviteMedia

# Register your models here.



class ActiviteMediaInline(admin.TabularInline):
	model = ActiviteMedia
	extra = 1


class ActiviteAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",),}

	inlines = [ActiviteMediaInline]







admin.site.register(Activite, ActiviteAdmin)
# admin.site.register(ActiviteMedia)

