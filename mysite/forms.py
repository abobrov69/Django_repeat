from django import forms
from galery.models import GalerieSeite, Bild
from nachrichten.models import Publication

class BildForm (forms.ModelForm):
    class Meta:
        model = Bild
        exclude = ()