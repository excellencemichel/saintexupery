from django.urls import path, re_path


from .views import (
			inscriptions,
	)


app_name = "inscriptions"






urlpatterns = [

		
		path("", inscriptions, name="inscriptions"),
		







				]