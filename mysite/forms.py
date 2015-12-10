# -*- coding: utf-8 -*-

from django import forms
from galery.models import GalerieSeite, Bild
from nachrichten.models import Publication

class BildForm (forms.ModelForm):
    class Meta:
        model = Bild
        exclude = ('dateiname_gross','dateiname_klein', 'img_klein')

    def clean(self):
        cleaned_data = super(BildForm, self).clean()
        grf = cleaned_data.get("img_gross")
        if not grf:
            self.add_error('img_gross', forms.ValidationError( ( 'Filename cannot by empty !'), code='invalid'))

        return self.cleaned_data

class NewsBildForm (forms.Form):
    titel = forms.CharField(widget=forms.TextInput(attrs={'class': "span5"}),label='Заголовок', max_length=50)
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': "span9"}) , max_length=250, label=u'Текст новости')
