from django.urls import re_path, path

from .views import (
    
    ActiviteDownloadView,
    activites,

    activite_detail,

    activite_update,

    create_activite,

    activite_delete,
)


app_name = "activites"



urlpatterns = [

    path("activites", activites, name="activites"),

    re_path(r'^detail/(?P<id>\d+)-(?P<slug>[\w-]+)/$', activite_detail, name="detail"),



    re_path(r'^edit/(?P<id>\d+)-(?P<slug>[\w-]+)/$', activite_update, name="update"),

    re_path(r'^create/$', create_activite, name="create"),

    re_path(r'^delete/(?P<id>\d+)-(?P<slug>[\w-]+)/$', activite_delete, name="delete"),




    
    re_path(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/download/$', ActiviteDownloadView.as_view(), name="download"),


]