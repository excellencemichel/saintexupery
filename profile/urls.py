from django.urls import path, re_path
from django.contrib.auth.views import (password_reset, password_reset_done,
                                      password_reset_confirm, password_reset_complete



                                      )

from .views import (
				home,
                register,
                activate,



		)


app_name = "profile"



urlpatterns = [


                path('register', register, name="register"),

                re_path(r'^activate/(?P<uidb64>[\w\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[\w]{1,20})/$', activate, name="active"),


]