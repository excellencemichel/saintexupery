from django.urls import path, re_path


from .views import (
			inscriptions,
			inscription_with_pdf_model,
	)


app_name = "inscriptions"






urlpatterns = [

		
		path("", inscriptions, name="inscriptions"),
		path("inscription_with_pdf_model", inscription_with_pdf_model, name="inscription_with_pdf_model"),
		







				]