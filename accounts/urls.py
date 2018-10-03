from django.urls import path, re_path
from .views import login, facebook_login



app_name = "accounts"


urlpatterns = [
      path('login/',login, name="login"),
      path('facebook-login/', facebook_login, name="facebook_login"),
    ]