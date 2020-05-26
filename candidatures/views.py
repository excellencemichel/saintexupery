
from io import BytesIO
from email.mime.base import MIMEBase
from email import encoders
from time import strftime

from django.conf import settings
from django.contrib import messages

from django.core.mail import  EmailMessage

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404






from .forms import CandidatureForm
# Create your views here.




def candidature(request):

	form = CandidatureForm(request.POST or None, request.FILES or None)
	phone_input = request.POST.get("phone_input")


	if form.is_valid() and phone_input is not None:
		human = True
		instance = form.save(commit=False)
		instance.telephone = phone_input
		instance.save()

		subject_postulant = """Confirmation par le centre ECF-Saint-Exupéry de la reception de votre candidature"""


		with open(settings.BASE_DIR + "/candidatures/templates/candidatures/candidature_email_message_to_postulant.txt") as f_postulant:
				candidature_message_to_postulant = f_postulant.read()
				f_postulant.close()


		#Réponse au postulant
		to_email_postulant = [instance.email]


		email_to_postulant = EmailMessage(

			subject = subject_postulant,
			body =candidature_message_to_postulant,
			from_email = settings.EMAIL_HOST_USER,
			to=to_email_postulant	
			)
		email_to_postulant.send()



		#Notification à la direction
		subject_direction = """"Une personne vient de postuler pour le centre ECF-Saint-Exupéry"""

		with open(settings.BASE_DIR + "/candidatures/templates/candidatures/candidature_email_message_to_direction.txt") as f_direction:
				candidature_message_to_direction = f_direction.read()
				f_direction.close()

		to_email_direction = ["michel37124077@gmail.com", "contact@ecf-saintex.com"]

		email_to_direction = EmailMessage(
			subject = subject_direction,
			body = candidature_message_to_direction,
			from_email= settings.EMAIL_HOST_USER,
			to = to_email_direction
			)

		instance_attach = MIMEBase('application', "octet-stream")
		instance_attach.set_payload(instance.cv.read())
		encoders.encode_base64(instance_attach)
		instance_attach.add_header('Content-Disposition', 'attachment', filename="{cv_name}.pdf".format(cv_name=instance.nom))

		email_to_direction.attach(instance_attach)

		email_to_direction.send()

		msg = ("""Votre candidature a bien été envoyée, un mail de confirmation vous a été aussi pour rester en contact""")
		messages.success(request, msg)


		return redirect(reverse("home"))
	else:
		print("Il y a une erreur dans le firmulaire")


	return render(request, "candidatures/candidature.html", {"form": form})



