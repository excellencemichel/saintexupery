from django.urls import path, re_path


from .views import (
			inscriptions, inscription
	)


app_name = "inscriptions"






urlpatterns = [

		
		path("", inscriptions, name="inscriptions"),

      	path("inscription", inscription, name="inscription"),

		







				]