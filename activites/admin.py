from django.contrib import admin
from .models import Activite, ActiviteMedia

# Register your models here.


class ActiviteAdmin(admin.ModelAdmin):
	# inlines = [ThumbnailInline]
	prepopulated_fields = {"slug":("title",),}







admin.site.register(Activite, ActiviteAdmin)
admin.site.register(ActiviteMedia)

