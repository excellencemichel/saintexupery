from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.urls import reverse, reverse_lazy

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# local
from .forms import ArticleForm
from .models import Article, ArticleMedia
from comments.models import Comment
from comments.forms import CommentForm


# Create your views here.

@login_required
def create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    files = request.FILES.getlist('images')
    if form.is_valid():
        # import pdb; pdb.set_trace()
        # instance = form.save(commit=False)
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        publish = form.cleaned_data.get("publish")

        image = files[0] 

        instance = Article.objects.create(user=request.user, title=title, image = image, content=content, publish=publish)
        instance.save()
        

        for f in files:
            instance_fichier = ArticleMedia.objects.create(photos=f, article=instance)
            instance_fichier.save()
        messages.success(request, "L'article a bien été créé")

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }

    return render(request, "evenements/create.html", context)


def articles(request):
    instances = Article.objects.all()

    context = {
        "instances": instances,
    }

    return render(request, "evenements/articles.html", context)


def detail(request, id=None, slug=None):
    instance = get_object_or_404(Article, id=id, slug=slug)

    share_string = quote_plus(instance.content)

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id,
    }

    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
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
    photos = ArticleMedia.objects.filter(article_id=instance.id)

    context = {
        "instance": instance,
        "photos": photos,
        "comments": comments,
        "form": form,
        "share_string": share_string,
    }

    return render(request, "evenements/article_detail.html", context)





@login_required
def update(request, id=None, slug=None):
    instance = get_object_or_404(Article, id=id, slug=slug)
    if instance.user != request.user:
        response = HttpResponse("Vous ne pouvez pas modifier cette publication car vous n'en êtes pas le propriétaire.")
        response.status_code = 403
        return response
    form = EvenementForm(request.POST or None, request.FILES or None, instance=instance)
    files = request.FILES.getlist("image")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        for f in files:
            instance_fichier = FichierModel(photos=f, evenement=instance)
            instance_fichier.save()
        messages.success(request, "L'évenement a bien été modifié !")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        # "ville": instance.ville,
        "instance": instance,
        "form": form,
    }

    return render(request, "evenements/create.html", context)


@login_required
def delete(request, id, slug):
    try:
        instance = Article.objects.get(id=id, slug=slug)
    except:
        raise Http404

    if instance.user != request.user:
        response = HttpResponse("Vous ne pouvez pas supprimer l'évenement car vous n'en êtes pas le propriétaire.")
        response.status_code = 403
        return response

    if request.method == "POST":
        instance.delete()
        messages.success(request, "This has been deleted.")
        return HttpResponseRedirect(reverse_lazy("home"))

    context = {
        "instance": instance,
    }

    return render(request, "evenements/confirme_delete.html", context)

def galerie_photo(request):

    context = {}

    return render(request, "evenements/galeries_photo.html", context)


def lesliens(request):

    context = {}



    return render(request, "evenements/lesliens.html", context)