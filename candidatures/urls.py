from django.urls import path

from .views import (
	candidature

)


app_name = "candidatures"



urlpatterns = [

			path("candidature", candidature, name="candidature"),




				]