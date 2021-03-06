

from io import BytesIO
from email.mime.base import MIMEBase
from email import encoders
from time import strftime

from django.conf import settings

from django.core.mail import  EmailMessage

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404





#Local
from .models import Inscription, Information
from .forms import InscriptionModelForm

from pdfapp.utils import render_to_pdf





def inscriptions(request):
	instance = Information.objects.last()

	context = {
		"instance": instance,
	}
	return render(request, "inscriptions/inscriptions.html", context)




def inscription(request):

	form = InscriptionModelForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		human = True
		instance = form.save(commit=False)

		annee = strftime("%y")
		mois =  strftime("%m")
		last_object = Inscription.objects.filter().last()
		print("Voici le last_object : ", last_object)
		if last_object == None:
			last_id = 1
		else:
			last_id = last_object.id
			print("Voici le last_id : ", last_id)


		if last_id == 1:
			object_id = last_id
			print("Voici le object_id: ", object_id)
		else:
			object_id = last_id  + 1
			print("Voici le object_id: ", object_id)
			
		matricule = "{annee}{mois}{id}".format(annee=annee, mois=mois, id=object_id)

		instance.matricule = matricule


		context = {"models_instance": instance}
		context["route_fichier"] = settings.BASE_DIR

		pdf_inscription = render_to_pdf("inscriptions/inscription_email_pdf.html", context)
		filename = "mypdf_{}.pdf".format(matricule)
		instance.pdf_inscription.save(filename, BytesIO(pdf_inscription.content))

		subject = """"Confirmation de l'accusé de reception de l'inscription de {nom} {prenom}""".format(nom=instance.nom, prenom=instance.prenom)
		subject_direction = """Une incription vient d'être faite depuis le site internet"""


		with open(settings.BASE_DIR + "/inscriptions/templates/inscriptions/inscription_email_message_to_direction.txt") as f_to_direction:
				inscription_message_to_direction = f_to_direction.read()

		with open(settings.BASE_DIR + "/inscriptions/templates/inscriptions/inscription_email_message.txt") as f:
				inscription_message = f.read()


		from_email = settings.EMAIL_HOST_USER
		to_email = [instance.email, instance.email_parent_un, instance.email_parent_deux]
		to_email_direction = ["contact@ecf-saintex.com"]

		email_pdf = EmailMessage(

			subject = subject,
			body =inscription_message,
			from_email = from_email,
			to=to_email,	
			)

		email_to_direction = EmailMessage(
			subject = subject_direction,
			body = inscription_message_to_direction,
			from_email= from_email,
			to= to_email_direction,
			)

		# instance_attach = instance.pdf_inscription.read()
		instance_attach = MIMEBase('application', "octet-stream")
		instance_attach.set_payload(instance.pdf_inscription.read())
		encoders.encode_base64(instance_attach)
		instance_attach.add_header('Content-Disposition', 'attachment', filename="{matricule}.pdf".format(matricule=matricule))

		# print(instance.pdf.name, instance.pdf.size)
		email_pdf.attach(instance_attach)
		email_to_direction.attach(instance_attach)

		email_pdf.send()
		email_to_direction.send()


		return redirect(reverse("home"))


	return render(request, "inscriptions/inscriptionform.html", {"form": form})

