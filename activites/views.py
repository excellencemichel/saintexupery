from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.urls import reverse, reverse_lazy

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.views.generic.detail import DetailView


# local
from .forms import ActiviteForm
from .models import Activite, ActiviteMedia
from comments.models import Comment
from comments.forms import CommentForm


# Create your views here.

@login_required
def create_activite(request):
    form = ActiviteForm(request.POST or None, request.FILES or None)
    files = request.FILES.getlist("media")
    if form.is_valid():
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # publish = form.cleaned_data.get("publish")

        # media = files[0] 

        # instance = Activite.objects.create(user=request.user, title=title, media = media, content=content, publish=publish)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()



        for f in files:
            instance_fichier = ActiviteMedia.objects.create(photos=f, activite=instance)
            instance_fichier.save()
        messages.success(request, "La publication a bien été faite")

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }

    return render(request, "activites/create.html", context)


def activites(request):
    instances = Activite.objects.all()
    # instances = instances.afficher()

    context = {
        "instances": instances,
    }

    return render(request, "activites/activites.html", context)


def activite_detail(request, id=None, slug=None):
    instance = get_object_or_404(Activite, id=id, slug=slug)

    share_string = quote_plus(instance.content)

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id,
    }

    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
    # if form.is_valid() and request.user.is_authenticated():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_date = form.cleaned_data.get("content")

        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))

        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)

            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_date,
            parent=parent_obj,
        )

        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    comments = instance.comments
    photos = ActiviteMedia.objects.filter(activite_id=instance.id)
    # if request.user.is_authenticated:
    #     can_update = True

    context = {
        "instance": instance,
        "photos": photos,
        "comments": comments,
        "form": form,
        "share_string": share_string,
    }

    return render(request, "activites/activite_detail.html", context)


@login_required
def activite_update(request, id=None, slug=None):
    instance = get_object_or_404(Activite, id=id, slug=slug)
    if instance.user != request.user:
        response = HttpResponse("Vous ne pouvez pas modifier cette activité car vous n'en êtes pas le propriétaire.")
        response.status_code = 403
        return response
    form = ActiviteForm(request.POST or None, request.FILES or None, instance=instance)
    files = request.FILES.getlist("media")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        for f in files:
            instance_fichier = ActiviteMedia(photos=f, activite=instance)
            instance_fichier.save()
        messages.success(request, "La publication a bien été modifiée !")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        # "ville": instance.ville,
        "instance": instance,
        "form": form,
    }

    return render(request, "activites/create.html", context)


@login_required
def activite_delete(request, id, slug):

    instance = get_object_or_404(Activite, id=id, slug=slug)

    if instance.user != request.user:
        response = HttpResponse("Vous ne pouvez pas supprimer la publication car vous n'en êtes pas le propriétaire.")
        response.status_code = 403
        return response

    if request.method == "POST":
        instance.delete()
        messages.success(request, "This has been deleted.")
        return HttpResponseRedirect(reverse_lazy("home"))

    context = {
        "instance": instance,
    }

    return render(request, "activites/confirme_delete.html", context)







class ActiviteDownloadView(DetailView):
    model = Activite

    def get(self, request, *args, **kwargs):
      
        obj = self.get_object()

        filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
        route = filepath.split(".")
        extention = route[-1]

        guessed_type = guess_type(filepath)[0]

        wrapper = FileResponse(open(filepath, "rb"))
        mimetype = "application/force-download"

        if guessed_type:
            mimetype = guessed_type

        response = HttpResponse(wrapper, content_type=mimetype) 

        if not request.GET.get("preview"):
            response["Content-Disposition"]= "attachement; filename=%s"%(obj.media.name)
                
        response["X-SendFile"] = str(obj.media.name)
        return response