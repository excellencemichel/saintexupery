from django.urls import re_path, path

from .views import (
    create,

    articles,

    detail,

    update,

    delete,
)


app_name = "evenements"



urlpatterns = [
    re_path(r'^create/$', create, name="create"),


    path("articles", articles, name="articles"),

    re_path(r'^detail/(?P<id>\d+)-(?P<slug>[\w-]+)/$', detail, name="detail"),



    re_path(r'^edit/(?P<id>\d+)-(?P<slug>[\w-]+)/$', update, name="update"),


    re_path(r'^delete/(?P<id>\d+)-(?P<slug>[\w-]+)/$',delete, name="delete"),
]