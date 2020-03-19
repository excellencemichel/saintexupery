from django.urls import re_path, path

from .views import (
						formulaire,
						contacts,
						detail,
					)


app_name = "contacts"


urlpatterns = [

			path("formulaire", formulaire, name="formulaire"),
			path("contacts", contacts, name="contacts"),

			re_path(r'^detail/(?P<id>\d+)/$', detail, name="detail"), #Quand on met pk il faut aussi mettre pk dans les representation d'url comme au niveau de get_absolute_url dans le model



]


