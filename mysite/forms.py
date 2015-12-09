from django import forms
from galery.models import GalerieSeite, Bild
from nachrichten.models import Publication

class BildForm (forms.ModelForm):
    class Meta:
        model = Bild
        exclude = ()

class MsgForm2 (forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('date','author','isdeleted','img_klein')
#        fields = ('text')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': "span9"}),
            }