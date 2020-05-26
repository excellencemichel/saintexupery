from django.urls import path, re_path

from .views import (

	
			horaires,

			calendrier_scolaire,

			infobules,
			infobule,

						
					)


app_name = "fonctionnements"


urlpatterns = [


				
				path("horaires", horaires, name="horaires"),


				path("calendrier_scolaire", calendrier_scolaire, name="calendrier_scolaire"),


				path("infos", infobules, name="infobules"),
				
				re_path(r'^(?P<id>\d+)-(?P<slug>[\w-]+)/info/$', infobule, name="infobule"),			



				]
