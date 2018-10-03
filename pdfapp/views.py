import datetime


from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template, render_to_string
from .utils import render_to_pdf




# Create your views here.




class GeneratePdfGuideInscription(View):
	def get(self, request, *args, **kwargs):
		template = get_template("pdfapp/guideinscription.html")
		context = {
				"invoice_id":123,
				"today" : datetime.date.today(),
				"amount" : 39.99,
				"customer_name": "Excellence Michel",
				"order_id": 1233434,
		}
		html = template.render(context)

		pdf = render_to_pdf("pdfapp/guideinscription.html", context)
		if pdf:
			response=HttpResponse(pdf, content_type="application/pdf")
			filename = "guide_inscription_cned.pdf"
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachement; filename='%s'"%(filename)
			response["Content-Disposition"] = content
			# response.save()
			return response
		return HttpResponse("Not found")


