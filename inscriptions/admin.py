from django.contrib import admin
from .models import Inscription, Information

# Register your models here.

MAX_MAX = 1


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_MAX:
			return False

		return super().has_add_permission(request)




admin.site.register(Inscription)

