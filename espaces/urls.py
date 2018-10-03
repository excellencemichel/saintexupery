from django.urls import re_path, path


from .views import (

		espace_etudiant

	)


app_name = "espaces"



urlpatterns = [
    path("", espace_etudiant, name="espace_etudiant"),

]