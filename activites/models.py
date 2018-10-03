from time import strftime
from random import randrange
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
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


class ActiviteManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ActiviteManager, self).filter(publish__lte=timezone.now)


class Activite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    media = models.ImageField(blank=True, null=True,
     upload_to=upload_location)

    content = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)



    # objects = ActiviteManager()

    def __str__(self):
        return self.title


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




    def get_absolute_url(self):
        
        view_name = "activites:detail"

        return reverse(view_name, kwargs={"id":self.id , "slug":self.slug})

    def get_download(self):
        view_name = "activites:download"
        url = reverse(view_name, kwargs={"id":self.id, "slug":self.slug})
        return url



    class Meta:
        ordering = ["-created", "-updated"]









def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug

    qs = Activite.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def activite_pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug or instance.slug != instance.title:
        instance.slug = create_slug(instance)






class ActiviteMedia(models.Model):
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE)
    photos = models.FileField(upload_to=upload_location)
pre_save.connect(activite_pre_save_post_receiver, sender=Activite)