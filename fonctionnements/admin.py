from django.contrib import admin
from django.db import models

from mdeditor.widgets import MDEditorWidget

from martor.widgets import AdminMartorWidget



from .models import Infobule, Calendrier, Horaire

from .forms import InfobuleForm, CalendrierForm, HoraireForm

from saintexupery.utils import unique_slug_generator_for_null

# Register your models here.



#Constante
MAX_MAX = 1



class InfobuleAdmin(admin.ModelAdmin):

	form = InfobuleForm

	formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget},
    }
	exclude = ["slug"]

	def save_model(self, request, obj, form, change):

		if not obj.slug:
			obj.slug = unique_slug_generator_for_null(obj)
		super().save_model(request, obj, form, change)







@admin.register(Calendrier)
class CalendrierAdmin(admin.ModelAdmin):
	form = CalendrierForm
	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_MAX:
			return False

		return super().has_add_permission(request)





@admin.register(Horaire)
class HoraireAdmin(admin.ModelAdmin):
	form = HoraireForm
	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_MAX:
			return False
		return super().has_add_permission(request)






admin.site.register(Infobule, InfobuleAdmin)
