from django.views.generic import TemplateView, ListView, DetailView
from galery.models import GalerieSeite, Bild
from django.http import HttpResponse, HttpResponseRedirect


class AuthorView(TemplateView):
    a = 1
    template_name = "author.html"

    def get_context_data(self, **kwargs):
        #        kwargs ['path'] = [v for k,v in self.request.META.items() if k == 'PATH_INFO'][0]
        return super(AuthorView, self).get_context_data(**kwargs)


class PageListView(ListView):
    model = GalerieSeite
    template_name = "pages_list.html"
    pg_in_row = 3

    def dispatch(self, request, *args, **kwargs):
        qs = self.model._default_manager.filter(isdeleted=False)
        self.seite_liste = []
        i = 1
        for k in qs:
            if i == 1:
                self.seite_liste.append([])
            self.seite_liste[-1].append(k)
            i = 1 if i >= self.pg_in_row else i + 1
        return ListView.dispatch(self, request, *args, **kwargs)

def detail(request, pk):
    return HttpResponse("You're looking for image number %s." % pk)


class CheckDeletedPageMixin(object):
    model = GalerieSeite

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.isdeleted:
            return HttpResponseRedirect('/' + '/galerie')
        else:
            return self.upper_class.get(self, request, *args, **kwargs)


class PageView(CheckDeletedPageMixin, DetailView):
    slug_field = 'seite_url'
    slug_url_kwarg = 'seite_url'
    template_name = "page_detail.html"
    context_object_name = 'seite'
    upper_class = DetailView
    pg_num = 1
    img_in_row = 3
    n_span = 4

    def dispatch(self, request, *args, **kwargs):
        if self.img_in_row > 12: self.img_in_row = 12
        self.n_span = int(12 / self.img_in_row)
        self.pg_num = 1 if not 'pg_num' in kwargs.keys() else int(kwargs['pg_num'])
        qs = self.model._default_manager.filter(seite_url=kwargs['seite_url'])
        if qs:
            bs = qs.get().bild_set.all()
            self.bilds = []
            i = 1
            for k in bs:
                if i == 1: self.bilds.append([])
                self.bilds[-1].append(k)
                i = 1 if i >= self.img_in_row else i + 1
        return self.upper_class.dispatch(self, request, *args, **kwargs)

class OneImageView(DetailView):
    model = Bild
    template_name = "image_detail.html"
    context_object_name = 'bild'
    pg_num = 1

    def dispatch(self, request, *args, **kwargs):
        self.pg_num = kwargs['pg_num']
        return DetailView.dispatch(self, request, *args, **kwargs)