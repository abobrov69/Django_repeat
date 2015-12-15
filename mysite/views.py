# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView
from forms import BildForm, NewsBildForm
from galery.models import GalerieSeite, Bild
from nachrichten.models import Publication
from nachrichten.views import ImageResize, MsgCreate
from datetime import datetime
from PIL import Image as PILImage
#from django.contrib import admin



class RootPageView(TemplateView):
    template_name = "mysite_root.html"
    def get_context_data(self, **kwargs):
#        kwargs ['path'] = [v for k,v in self.request.META.items() if k == 'PATH_INFO'][0]
        return super(RootPageView,self).get_context_data(**kwargs)

class AboutView(TemplateView):
    template_name = "about.html"
#    a=admin.site.urls
#    vb = egsdg
    def get_context_data(self, **kwargs):
#        kwargs ['path'] = [v for k,v in self.request.META.items() if k == 'PATH_INFO'][0]
        return super(AboutView,self).get_context_data(**kwargs)

class BildCreateView (CreateView):
    form_class = BildForm
    template_name = "bild_edit.html"
    model = Bild
    success_url = '/macht'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.username:
            self.template_name = "404.html"
            self.success_url = '/'
#        self.success_url = '/'
        return super(BildCreateView,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if form.instance.img_gross:
            self.object = form.save()
            if form.instance.img_gross.name [0:2] == './': form.instance.img_gross.name = form.instance.img_gross.name [2:]
            img_gr = PILImage.open(form.instance.img_gross.path)
            img_kl = ImageResize(img_gr, form.instance.img_gross.width, form.instance.img_gross.height )
            form.instance.img_klein.name = 'kl_'+form.instance.img_gross.name
            img_kl.save (form.instance.img_klein.path)
            form.instance.dateiname_gross = form.instance.img_gross.name
            form.instance.dateiname_klein = form.instance.img_klein.name
            self.success_url = '/news_img_crea/'+str(form.instance.pk)
        return super (BildCreateView,self).form_valid(form)

class NewsCreate (MsgCreate):
    success_url = '/macht'

    def get_success_url(self):
        a = self.object.pk
        self.success_url = '/nachrichten/details/'+str (a)
        return super (NewsCreate,self).get_success_url()

class NewsofBildCreateView (FormView):
    form_class = NewsBildForm
    success_url = '/macht'
    template_name = "news_bild_edit.html"
    bld_pk = -1
    bild = 0

    def get_context_data(self, **kwargs):
        context = super(NewsofBildCreateView, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.username:
            self.template_name = "404.html"
            self.success_url = '/'
        else:
            self.bld_pk = kwargs['bld_pk']
            self.bild = Bild.objects.get (pk=self.bld_pk)
            self.initial['titel'] = u'Новая работа в разделе "'+self.bild.seite.titel+'".'
            if self.bild.titel[-1] == '"':
                bld_t = self.bild.titel[:-1]
            else:
                bld_t = self.bild.titel
            self.initial['text'] = u'В раздел <strong>"'+self.bild.seite.titel+u'"</strong> добавлена новая '+u'работа <strong>"'+bld_t+'"</strong>.'
#            a = b
        return FormView.dispatch(self, request, *args, **kwargs)

    def form_valid(self, form):
        news = Publication (
                date = datetime.now(),
                author = self.request.user,
                titel = form.cleaned_data['titel'],
                text = form.cleaned_data['text'],
                img_gross = self.bild.img_gross,
                img_klein = self.bild.img_klein,
                url_bild_pg = '/galerie/image/1/'+str(self.bld_pk)
        )
        news.save()
        if form.cleaned_data['l_go_news_pg']: self.success_url = '/nachrichten/details/'+str (news.pk)
        return super (NewsofBildCreateView,self).form_valid(form)