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
    photos = ArticleMedia.objects.filter(article_id=instance.id)

    context = {
        "instance": instance,
        "photos": photos,
        "share_string": share_string,
    }

    return render(request, "evenements/detail.html", context)





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
