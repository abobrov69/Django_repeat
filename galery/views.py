from django.views.generic import TemplateView, ListView, DetailView
from galery.models import GalerieSeite, Bild
from django.http import HttpResponse, HttpResponseRedirect


class AuthorView(TemplateView):
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
        self.pg_array = []
        i = 1
        for k in qs:
            if i == 1:
                self.pg_array.append([])
            self.pg_array[-1].append(k)
            i = 1 if i >= self.pg_in_row else i + 1
        return ListView.dispatch(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        context['seite_liste'] = self.pg_array
        #        a=b
        return context


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
    img_in_row = 4
    n_span = 3

    def dispatch(self, request, *args, **kwargs):
        if self.img_in_row > 12: self.img_in_row = 12
        self.n_span = int(12 / self.img_in_row)
        self.pg_num = 1 if not 'pg_num' in kwargs.keys() else int(kwargs['pg_num'])
        qs = self.model._default_manager.filter(seite_url=kwargs['seite_url'])
        if qs:
            bs = qs.get().bild_set.all()
            self.img_array = []
            i = 1
            for k in bs:
                if i == 1: self.img_array.append([])
                self.img_array[-1].append(k)
                i = 1 if i >= self.img_in_row else i + 1
        return self.upper_class.dispatch(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['pg_num'] = self.pg_num
        context['bilds'] = self.img_array
        context['n_span'] = self.n_span
        return context

class OneImageView(DetailView):
    model = Bild
    template_name = "image_detail.html"
    context_object_name = 'bild'

