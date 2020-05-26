from django.urls import path

from .views import (
				primaire,
				college,
				lycee,
				presentation,

)


app_name = "cycles"



urlpatterns = [

			path("primaire", primaire, name="primaire"),


			path("college", college, name="college"),

			path("lycee", lycee, name="lycee"),
			path("presentation", presentation, name="presentation"),




				]