"""zaly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.contrib.auth.views import (
            password_reset,
            password_reset_done,
            password_reset_confirm,
            password_reset_complete,
    )



from django.urls import include, path, re_path


from .views import home, navs


from inscriptions.views import inscription


urlpatterns = [
    path('admin/', admin.site.urls),


    path("", home, name="home"),
    path("navs", navs, name="navs"),



    path('profile/', include("profile.urls", namespace="profile")),
    path('account/', include("accounts.urls", namespace="accounts")),

    path('contacts/', include("contacts.urls", namespace="contacts")),

    path('commens/', include("comments.urls", namespace="comments")),

    path('evenements/', include("evenements.urls", namespace="evenements")),

    path('presentation/', include("presentation.urls", namespace="presentation")),

    path('cycles/', include("cycles.urls", namespace="cycles")),

    path('fonctionnements/', include("fonctionnements.urls", namespace="fonctionnements")),





    path('inscriptions/', include("inscriptions.urls", namespace="inscriptions")),
    path('pdfapp/', include("pdfapp.urls", namespace="pdfapp")),
    path('espaces/', include("espaces.urls", namespace="espaces")),











      path('reset-password', password_reset, name="reset_password"),
      path('reset-password/done', password_reset_done, name="password_reset_done"),
      re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),
      path('reset-password/complete', password_reset_complete, name="password_reset_complete"), 


      path("inscription", inscription, name="inscription"),






]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

