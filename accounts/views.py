from datetime import datetime

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


from  django.conf import settings

from django.utils.translation import ugettext as _
from django.utils.http import is_safe_url


from django.contrib.auth import  get_user_model
from django.contrib import messages
from django.contrib import auth as auth_c

from django.views.generic import  FormView




#Locales import
from saintexupery.mixins import NextUrlMixin, RequestFormAttachMixin

from .forms import ConnexionForm

User = get_user_model()


# Create your views here.



def login(request):
	error = False
	form = ConnexionForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]


		user = auth_c.authenticate(username=username, password=password)

		if user:
			auth_c.login(request, user)
			messages.success(request, _("Bienvenu  {}".format(username)))
			default_url ="/"
			request =request
			print("Voici",request.POST.get("next"))
			next_ = request.GET.get("next")
			next_post = request.POST.get("next")
			redirect_path = next_ or next_post or None
			if is_safe_url(redirect_path, request.get_host()):
				# return redirect(reverse("home"))
				return redirect(redirect_path)
			return redirect(default_url)


		else:
			error = True
	else:
		form = ConnexionForm()

	context = {
	    "form":form,
	    "error":error,
	}


	return render(request, "accounts/login.html", context)





def facebook_login(request):
	redirect_uri = "%s://%s%s"%(
		request.scheme, request.get_host(), reverse("accounts:facebook_login")
	)
	if("code" in request.GET):
		code = request.GET.get("code")
		url = "https://graph.facebook.com/oauth/access_token"

		params = {
			"client_id": settings.FB_APP_ID,
			"client_secret": settings.FB_APP_SECRET,
			"code": code,
			"redirect_uri" : redirect_uri,
		}

		response = request.get(url, params=params)
		params = response.json()
		params.update({
			"fields": "id, last_name, first_name, picture, birthday, email, gender"
		})

		url = "https://graph.facebook.com/me"

		user_data = request.get(url, params=params).json()

		email = user_data.get("email")
		if email:
			user, _ = User.objects.get_or_create(email=email, username=email)
			gender = user_data.get("gender", "").lower()
			dob = user_data.get("birthday")
			if gender == "Male":
				gender = "M"
			elif gender == "female":
				gender = "F"

			else:
				gender = "O"

			data = {
				"first_name": user_data.get("first_name"),
				"last_name" : user_data.get("last_name"),
				"fb_avatar": user_data.get("picture", {}).get("data", {}).get("url"),
				"gender" : gender,
				"dob": datetime.strftime(dob, "%m/%d/%Y")if dob else None,
				"is_active": True

			}

			user.__dict__.update(data)

			user.save()

			user.backend = settings.AUTHENTICATION_BACKENDS[0]
			login(request, user)

		else:
			messages.error(request,
						   "Unable to login with Facebook Please try again"
						   )


		return  redirect("home")
	else:
		url = "https://graph.facebook.com/oauth/authorize"
		params = {
			"client_id": settings.FB_APP_ID,
			"redirect_uri" : redirect_uri,
			"scope": "email, public_profile, user_birthday"
		}

	url += "?" + urlencode(params)
	return redirect(url)



class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = ConnexionForm
    success_url = "/"
    template_name = "accounts/login.html"

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)     
