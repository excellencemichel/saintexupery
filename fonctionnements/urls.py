from django.urls import re_path, path

from .views import (

	
			horaires,

			calendrier_scolaire,

						
					)


app_name = "fonctionnements"


urlpatterns = [


				
				path("horaires", horaires, name="horaires"),


				path("calendrier_scolaire", calendrier_scolaire, name="calendrier_scolaire"),


				]
