from django.contrib import admin
from django.db import models

from mdeditor.widgets import MDEditorWidget
from martor.widgets import AdminMartorWidget


from .models import Article, ArticleMedia

from saintexupery.utils import unique_slug_generator


# Register your models here.


class ArticleMediaInline(admin.TabularInline):
	model = ArticleMedia
	extra = 1


class ArticleAdmin(admin.ModelAdmin):

	formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget},
    }
	inlines = [ArticleMediaInline]
	exclude = ["user", "slug"]

	def save_model(self, request, obj, form, change):

		if not obj.pk:
			# Only set added_by during the first save.
			obj.user = request.user

		if not obj.slug:
			obj.slug = unique_slug_generator(obj)
		super().save_model(request, obj, form, change)








admin.site.register(Article, ArticleAdmin)
