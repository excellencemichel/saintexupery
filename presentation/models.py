from os import path

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save


from saintexupery.utils import unique_slug_generator




# Create your models here.


def get_filename(filepath):
    base_name = path.basename(filepath)
    name_file, extension_file = path.splitext(base_name)
    return name_file, extension_file



def upload_file_location(instance, filename):
    instance_name = instance.title
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
    

    return "presentations/{instance_name}/{final_filename}".format(instance_name=instance_name, final_filename=final_filename)



class Generale(models.Model):
    PRESENTATION = "presentation"
    MOT_DIRECTEUR = "mot_directrice"
    EQUIPE_PEDAGOGIQUE = "equipe_pedagogique"
    PROGRAMME = "programme"

    TYPE_PRESENTATION = (

        (PRESENTATION, "Présentation"),
        (MOT_DIRECTEUR, "Mot du directeur"),
        (PROGRAMME, "Programe du CNED"),
        (EQUIPE_PEDAGOGIQUE, "Equipe pédagogique"),

        )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


    content = models.TextField()
    image = models.FileField(upload_to=upload_file_location, null=True, blank=True)
    presentation_type = models.CharField(max_length=250, choices=TYPE_PRESENTATION)


    created = models.DateTimeField(auto_now=False, auto_now_add=True)


    updated = models.DateTimeField(auto_now=True, auto_now_add=False)




    def __str__(self):
        return self.title


    class Meta:
    	verbose_name = "L'Ecole"
    	verbose_name_plural = "L'Ecole"





class Partenaire(models.Model):
    title         = models.CharField(max_length=250)
    slug        = models.SlugField()
    contenu     = models.TextField()
    logo        = models.ImageField(upload_to=upload_file_location, null=True, blank=True)
    created     = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)



    def __str__(self):
        return "Partenaire {title}".format(title=self.title)








def partenaire_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(partenaire_pre_save_receiver, sender=Partenaire)