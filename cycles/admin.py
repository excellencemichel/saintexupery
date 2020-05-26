from django.contrib import admin



from .models import Cycle, Presentation


# Register your models here.
MAX_CYLES = 4
MAX_PRESENTATION = 1




@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
	exclude = ["slug"]
	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_CYLES:
			return False

		return super().has_add_permission(request)





@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
	exclude = ["slug"]
	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_PRESENTATION:
			return False
		return super().has_add_permission(request)



