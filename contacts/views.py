from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings



from .models import Contact

from .forms import ContactForm

# Create your views here.

@csrf_protect
def formulaire(request, template_name="contacts/formulaire.html",
	           email_template_name="contacts/contact_email.html" ,
	           subject_template_name="contacts/contact_email_subject.txt",
	           form=ContactForm,
	           from_email = settings.EMAIL_HOST_USER,
	           extra_context=None,
	           html_email_template_name="contacts/contact_email_html.html" ,
	           extra_email_context=None):



	if request.method == "POST":
		form = form(request.POST, request.FILES)
		if form.is_valid():
			opts = {
				"use_https": request.is_secure(),
				"from_email": from_email,
				"email_template_name": email_template_name,
				"subject_template_name":subject_template_name,
				"request":request,
				"html_email_template_name" :html_email_template_name,
				"extra_email_context": extra_email_context,
			}

			form.save(**opts)


			nom = form.cleaned_data["nom"]
			prenom = form.cleaned_data["prenom"]
			telephone = form.cleaned_data["telephone"]
			email = form.cleaned_data["email"]
			subject = form.cleaned_data["subject"]
			message = form.cleaned_data["message"]


			nouveau_contact = Contact(nom=nom, prenom=prenom, telephone=telephone, email=email, subject=subject, message=message).save()


			return redirect(reverse("home"))


	else:
		form = form


	context = {
		"form" :form,
	}

	if extra_context is not None:
		context.update(extra_context)

	return TemplateResponse(request, template_name, context)







@login_required
def contacts(request):

	contacts = Contact.objects.all()


	context = {
		"contacts":contacts
	}


	return render(request, "contacts/contacts.html", context)






def detail(request, id=None):

	contact = get_object_or_404(Contact, id=id)


	context = {

		"contact" : contact
	}


	return render(request, "contacts/detail.html", context)
