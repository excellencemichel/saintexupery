from django.urls import re_path, path

from .views import (
				maternelle,
				primaire,
				college,
				lycee,
				presentation_cycles,

)


app_name = "cycles"



urlpatterns = [

	
			path("maternelle", maternelle, name="maternelle"),
			path("primaire", primaire, name="primaire"),


			path("college", college, name="college"),

			path("lycee", lycee, name="lycee"),
			path("presentation-cycles", presentation_cycles, name="presentation_cycles"),




				]