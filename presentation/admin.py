from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Generale, Partenaire
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Generale)
class GeneraleAdmn(admin.ModelAdmin):
	exclude = ['user',]
	readonly_fields = ["show_image"]


	def get_actions(self, request):
		actions = super().get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


	def show_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )


	def has_add_permission(self, request):
		return False


	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
	exclude = ["slug"]





admin.site.unregister(Group)

