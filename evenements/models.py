from time import strftime
from random import randrange
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

from comments.models import Comment


# Create your models here.

def upload_location(instance, filename):
    extension = filename.split(".")[-1]
    jour = strftime("%a")
    temps = strftime("%d-%m-%Y-%H-%M-%S")
    pseudo = randrange(-1000000, 1000000)
    print(extension)
    return "{}/{}_{}.{}".format(jour, temps, pseudo, extension)


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()


    image = models.FileField(upload_to=upload_location)
    content = models.TextField()

    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    publish = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("evenements:detail", kwargs={"id": self.id, "slug": self.slug})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    class Meta:
        ordering = ["-created", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug

    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug or instance.slug != instance.title:
        instance.slug = create_slug(instance)


class ArticleMedia(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    photos = models.FileField(upload_to=upload_location)


pre_save.connect(pre_save_post_receiver, sender=Article)


