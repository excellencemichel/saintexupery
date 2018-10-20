from django.urls import path, re_path
from .views import login, facebook_login, LoginView



app_name = "accounts"


urlpatterns = [
      # path('login/',login, name="login_old"),
	  path("login/", LoginView.as_view(), name="login"),
      path('facebook-login/', facebook_login, name="facebook_login"),
    ]