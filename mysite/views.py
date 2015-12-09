from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from forms import BildForm, MsgForm2
from galery.models import GalerieSeite, Bild
from nachrichten.models import Publication
from nachrichten.views import small_image_width, small_image_height, MsgCreate
from datetime import datetime
from PIL import Image as PILImage
from django.contrib import admin



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

class ImageCreateView (CreateView):
    form_class = BildForm
    template_name = "bild_edit.html"
    model = Bild
    success_url = '/macht'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.username:
            self.template_name = "about.html"
        self.success_url = '/'
        return super(ImageCreateView,self).dispatch(request, *args, **kwargs)

class NewsCreate (MsgCreate):
    success_url = '/macht'

