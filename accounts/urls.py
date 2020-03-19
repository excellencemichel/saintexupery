from django.urls import path
from .views import facebook_login, LoginView



app_name = "accounts"


urlpatterns = [
	  path("login/", LoginView.as_view(), name="login"),
      path('facebook-login/', facebook_login, name="facebook_login"),
    ]