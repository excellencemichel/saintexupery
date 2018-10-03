from django.urls import path, re_path


from .views import (

			GeneratePdfGuideInscription,
	)


app_name = "pdfapp"






urlpatterns = [

        path("preview", GeneratePdfGuideInscription.as_view(), name="guide_inscription_pdf"),
        

]
