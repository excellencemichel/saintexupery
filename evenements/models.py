from os import path



from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from saintexupery.utils import unique_slug_generator


from comments.models import Comment




# Create your models here.


def get_filename(filepath):
    base_name = path.basename(filepath)
    name_file, extension_file = path.splitext(base_name)
    return name_file, extension_file



def upload_file_location_with(instance, filename):
    id_ = instance.id
    if id_ is None:
        Klass = instance.__class__
        qs = Klass.objects.all().order_by("-pk")
        if qs.exists():
            id_ = qs.first().id + 1
        else:
            id_ = 0
    name_file, extension_file =get_filename(filename)

    final_filename = "{name_file}_{id_}{extension_file}".format(name_file=name_file, id_=id_, extension_file=extension_file)
    

    return "evenements/{final_filename}".format(final_filename=final_filename)




class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()


    image = models.FileField(upload_to=upload_file_location_with)
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


def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(article_pre_save_receiver, sender=Article)


class ArticleMedia(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    photos = models.FileField(upload_to=upload_file_location_with)




