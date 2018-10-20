from django.urls import re_path, path

from .views import (
    create,

    articles,

    detail,

    update,

    delete,
    galerie_photo,
    lesliens,

)


app_name = "evenements"



urlpatterns = [
    re_path(r'^create/$', create, name="create"),


    path("articles", articles, name="articles"),

    re_path(r'^detail/(?P<id>\d+)-(?P<slug>[\w-]+)/$', detail, name="detail"),



    re_path(r'^edit/(?P<id>\d+)-(?P<slug>[\w-]+)/$', update, name="update"),


    re_path(r'^delete/(?P<id>\d+)-(?P<slug>[\w-]+)/$',delete, name="delete"),

    path("galerie_photo", galerie_photo, name="galerie_photo"),

    path("lesliens", lesliens, name="lesliens")

]