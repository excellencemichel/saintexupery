from django.urls import re_path, path

from .views import (

					presentation,
					partenaires,
					mot_directeur,
					programme,
					equipe_pedagogique,

						
					)


app_name = "presentation"


urlpatterns = [


			path("presentation", presentation, name="presentation"),
			path("partenaires", partenaires, name="partenaires"),
			path("mot_directeur", mot_directeur, name="mot_directeur"),
			path("programme", programme, name="programme"),
			path("equipe_pedagogique", equipe_pedagogique, name="equipe_pedagogique"),







		]