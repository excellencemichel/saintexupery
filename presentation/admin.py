from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe


from .models import Generale, Partenaire


# Register your models here.
MAX_PARTENAIRES = 10

MAX_GENERALE = 4
MAX_MAX = 1


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
		if self.model.objects.count() >= MAX_GENERALE:
			return False

		return super().has_add_permission(request)

	def has_delete_permission(self, request, obj=None):
		return False


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
	exclude = ["slug"]
	def has_add_permission(self, request):
		if self.model.objects.count() >= MAX_PARTENAIRES:
			return False

		return super().has_add_permission(request)











admin.site.unregister(Group)



