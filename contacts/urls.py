from django.urls import re_path, path

from .views import (
						plan,
						formulaire,
						coordonnees,
						lien_reseaux_sociaux,
						contacts,
						detail,
					)


app_name = "contacts"


urlpatterns = [

			path("plan", plan, name="plan"),
			path("formulaire", formulaire, name="formulaire"),
			path("coordonnees", coordonnees, name="coordonnees"),
			path("liens-réseau-sociaux", lien_reseaux_sociaux, name="lien_reseaux_sociaux"),
			path("contacts", contacts, name="contacts"),

			re_path(r'^detail/(?P<id>\d+)/$', detail, name="detail"), #Quand on met pk il faut aussi mettre pk dans les representation d'url comme au niveau de get_absolute_url dans le model



]


