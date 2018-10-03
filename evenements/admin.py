from django.contrib import admin
from .models import Article, ArticleMedia

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",),}



admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleMedia)
