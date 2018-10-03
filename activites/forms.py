from django.utils.translation import pgettext, ugettext, ugettext_lazy as _

from django import forms

from .models import Activite



class ActiviteForm(forms.ModelForm):

    title = forms.CharField(label=_("Le titre de la publication"),
                            widget=forms.TextInput(attrs={"class": "form-control"}),
                            )

    content = forms.CharField(label=_("Contenu de la publication"),

                              help_text=_("Vous pouvez agrandir le la fenêtre"),
                              widget=forms.Textarea(attrs={"class": "form-control",
                                                           "rows": "7",
                                                           }
                                                    )
                              )

    publish = forms.DateTimeField(label=_("Le moment auquel vous voulez que la publication soit disponible"),
                              widget=forms.SelectDateWidget
                              )

    media = forms.FileField(label=_("Chargez les image de la publication s'il y en a"),
                            widget=forms.ClearableFileInput(attrs={'multiple': True})
                             )
    class Meta:
      model = Activite
      fields = ("title", "content", "media", "publish")