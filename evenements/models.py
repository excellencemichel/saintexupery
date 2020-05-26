from os import path



from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone


from mdeditor.fields import MDTextField



from saintexupery.utils import unique_slug_generator, upload_file_location







# Create your models here.


class ArticleQuerySet(models.query.QuerySet):
    def permettre(self):
        return self.filter(permettre=True)







class ArticleManager(models.Manager):

    def permettre(self):
        return self.filter(permettre=True)





class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()


    image = models.FileField(upload_to=upload_file_location)
    permettre  = models.BooleanField(default=True)
    content = models.TextField()

    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    publish = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    objects = ArticleManager()





    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("evenements:detail", kwargs={"id": self.id, "slug": self.slug})


    class Meta:
        ordering = ["-created", "-updated"]


def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(article_pre_save_receiver, sender=Article)


class ArticleMedia(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    photos = models.FileField(upload_to=upload_file_location)




