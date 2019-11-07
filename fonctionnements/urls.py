from django.urls import re_path, path

from .views import (
			fonctionnement,
			horaires,

			vacances,

						
					)


app_name = "fonctionnements"


urlpatterns = [


				path("fonctionnement", fonctionnement, name="fonctionnement"),
				
				path("horaires", horaires, name="horaires"),


				path("vacances", vacances, name="vacances"),


				]
