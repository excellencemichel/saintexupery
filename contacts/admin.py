from django.contrib import admin

from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_filter = ("created", "created",) #Pour les champs qui vont s'afficher dans l'admin



