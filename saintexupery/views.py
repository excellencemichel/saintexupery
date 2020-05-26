
from django.shortcuts import render, redirect, resolve_url


import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from martor.utils import LazyEncoder




from evenements.models import Article
from presentation.models import  Partenaire, Generale
from cycles.models import Cycle



# Create your views here.


@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif',
                'video/mp4', "video/wav",
                "video/wmv"
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Bad image format.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps({
                    'status': 405,
                    'error': _('Maximum image file is %(size) MB.') % {'size': to_MB}
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps({
                'status': 200,
                'link': img_url,
                'name': image.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))




def home(request):

	instance_articles= Article.objects.permettre()[:5]
	partenaires = Partenaire.objects.all()[:7]
	presentation = Generale.objects.filter(presentation_type=Generale.PRESENTATION).first()


	cycles = Cycle.objects.all()
	primaire = cycles.filter(niveau_cycle=Cycle.PRIMAIRE)
	college = cycles.filter(niveau_cycle=Cycle.COLLEGE)
	lycee = cycles.filter(niveau_cycle = Cycle.LYCEE)

	context = {

		"instance_evenements" : instance_articles,
		"partenaires":partenaires,
		"presentation": presentation,
		"primaire": primaire,
		"college" : college,
		"lycee": lycee,
	}
	return render(request, "home.html", context)