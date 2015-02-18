from django.views.generic import TemplateView, ListView, DetailView
from galery.models import GalerieSeite
from django.http import HttpResponse, HttpResponseRedirect

class AuthorView(TemplateView):
    template_name = "author.html"
    def get_context_data(self, **kwargs):
#        kwargs ['path'] = [v for k,v in self.request.META.items() if k == 'PATH_INFO'][0]
        return super(AuthorView,self).get_context_data(**kwargs)

class PageListView(ListView):
    model = GalerieSeite
    template_name = "pages_list.html"
    context_object_name = 'seite_liste'

def detail(request, seite_url):
    return HttpResponse("You're looking at question %s." % seite_url)

class CheckDeletedPageMixin (object):
    model = GalerieSeite

    def get (self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.isdeleted:
           return HttpResponseRedirect ('/'+'/galerie')
        else:
            return self.upper_class.get (self, request, *args, **kwargs)

class MsgView (CheckDeletedPageMixin,DetailView):
    slug_field = 'seite_url'
    slug_url_kwarg = 'seite_url'
    template_name = "page_detail.html"
    context_object_name = 'seite'
    upper_class = DetailView