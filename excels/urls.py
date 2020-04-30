from django.urls import path, re_path


from .views import  exports_data, export_inscription_data, embed_handson_inscription_table

app_name = "excels"


urlpatterns = [
		 
	    path("export-inscription/<str:atype>/", export_inscription_data,  name="export_inscription_data_sheet"),
	    path("export-inscription/<str:atype>/", export_inscription_data, name="export_inscription_data_custom"),


	  	path("inscriptions-visualization", embed_handson_inscription_table, name="embed_handson_inscription_table"),

	     path("exports-data", exports_data, name="exports"),





]

