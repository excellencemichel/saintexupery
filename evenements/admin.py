from django.contrib import admin
from .models import Article, ArticleMedia

# Register your models here.


class ArticleMediaInline(admin.TabularInline):
	model = ArticleMedia
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",),}
	inlines = [ArticleMediaInline]



admin.site.register(Article, ArticleAdmin)
# admin.site.register(ArticleMedia)
