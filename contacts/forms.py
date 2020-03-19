

from django.core.mail import EmailMultiAlternatives

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template import loader
from django.template.loader import get_template



from django.utils.translation import pgettext, ugettext, ugettext_lazy as _



from django import forms





class ContactForm(forms.Form):
	nom = forms.CharField(label=_("Votre nom"),
	    						widget =forms.TextInput(attrs={"class": "form-control input-sm", "placeholder":"Dupont"}),
    	                        )

	prenom = forms.CharField( label=_("Votre prénom"),

		                      widget =forms.TextInput(attrs={"class": "form-control input-sm", "placeholder":"Michel"}),
    	                        
		                     )

	# telephone = forms.CharField(label=_("Téléphone avec indicatif"),
	# 							widget =forms.TextInput(attrs={"class": "form-control input-sm", "placeholder":"+212..."}),
 #    	                       )


	email = forms.EmailField(widget = forms.EmailInput(attrs={"class": "form-control input-sm", "placeholder":"exemple@gmail.com"}),
		                    )
	subject = forms.CharField(
								widget =forms.TextInput(attrs={"class": "form-control input-sm", "placeholder":"Objet du message ..."}),
    	                       )

	message = forms.CharField(label=_("Message à laisser"),
		widget=forms.Textarea(attrs={"class": "form-control input-lg", "placeholder":"Mon Message..."}),
		)




	def send_mail(self, subject_template_name, email_template_name,context, from_email, to_email, html_email_template_name=None):
		"""
		Send a django.core.mail.EmailMultiAlternatives to 'to_email.'
		"""

		subject = loader.render_to_string(subject_template_name, context)
		#Email subject *mut not* contain newlines
		subject= ''.join(subject.splitlines())
		# body = loader.render_to_string(email_template_name, context)
		body = get_template(email_template_name).render(context)

		email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
		if html_email_template_name is not None:
			html_email=loader.render_to_string(html_email_template_name, context)
			email_message.attach_alternative(html_email, "text/html")


		email_message.send()


	def save(self, domaine_override=None, subject_template_name="contacts/contact_email_subject.html",email_template_name="contacts/contact_email.html", use_https=False,from_email=None, to_email="ecf.saintexpery@gmail.com", request=None, html_email_template_name="contacts/contact_email_html.html", extra_email_context=None):

		"""
		Generate a one-use only link for resettint passord and send to the user
		"""

		nom = self.cleaned_data["nom"]
		prenom = self.cleaned_data["prenom"]
		# telephone = self.cleaned_data["telephone"]
		email = self.cleaned_data["email"]
		subject = self.cleaned_data["subject"]
		message = self.cleaned_data["message"]

		if not domaine_override:
			current_site = get_current_site(request)
			site_name = current_site.name 
			domain = current_site.domain

		else:
			site_name = domain= domaine_override

		context = {
			"nom": nom,
			"prenom":prenom,
			"telephone": telephone,
			"email": email,
			"subject" : subject,
			"message" :message,
			"domain":domain,
			"site_name":site_name,
			# "uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
			# "token": token_generator.make_token(nom),
			"protocol": "https" if use_https else "http",
		}

		if extra_email_context is not None:
			context.update(extra_email_context)

		self.send_mail(
				subject_template_name, 
				email_template_name, 
				context, from_email, 
				to_email,
				html_email_template_name=html_email_template_name,
			)

