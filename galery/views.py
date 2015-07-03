from django.views.generic import TemplateView, ListView, DetailView
from galery.models import GalerieSeite, Bild
from django.http import HttpResponse, HttpResponseRedirect

bilds_in_seite = 6

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

def get_sort_bilds_list (curr_seite):
    bilds_sort_order = ('-sort_num','-pk')
    return curr_seite.bild_set.filter ( isdeleted=0 ).order_by (*bilds_sort_order)


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
    pg_num_prev = 0
    pg_num_larr = 0
    pg_num_rarr = 0
    pg_left_arrow = False
    pg_right_arrow = False
    pg_lst_len = 5
    pg_num_next = 2
    no_pg_num_str = ''
    img_in_row = 3
    n_span = 6
    num_pages = 0

    def dispatch(self, request, *args, **kwargs):
        if self.img_in_row > 12: self.img_in_row = 12
        self.n_span = int(12 / self.img_in_row)
        if not 'pg_num' in kwargs.keys():
            self.pg_num = 1
            self.no_pg_num_str = ''
        else:
            self.pg_num = int(kwargs['pg_num'])
            if self.pg_num <1: self.pg_num = 1
            self.no_pg_num_str = '../'
        qs = self.model._default_manager.filter(seite_url=kwargs['seite_url'])
        if qs.exists():
            bs = get_sort_bilds_list (qs.get())
            n5 = len (bs)
            n1 = n5 / bilds_in_seite
            self.num_pages = n1 + (1 if n5 % bilds_in_seite else 0)
            if self.num_pages < self.pg_num: self.pg_num = self.num_pages
            self.pg_num_prev = self.pg_num - 1
            self.pg_num_next = self.pg_num + 1
            if self.num_pages < self.pg_num_next: self.pg_num_next = 0
            if self.num_pages > self.pg_lst_len:
                n1 = self.pg_num - self.pg_lst_len / 2
                if n1 < 1: n1 = 1
                self.pg_left_arrow = (n1 > 1)
                n5 = n1 + self.pg_lst_len - 1
                if n5>self.num_pages:
                    n5 = self.num_pages
                    n1 = n5 - self.pg_lst_len + 1
                self.pg_right_arrow = ( n5 < self.num_pages)
            else:
                n1 = 1
                n5 = n1 + self.num_pages - 1
                self.pg_left_arrow = False
                self.pg_right_arrow = False

            if n1 < self.pg_num:
                self.pg_num_larr = []
                while n1 < self.pg_num:
                    self.pg_num_larr.append(n1)
                    n1+= 1
            else: self.pg_num_larr = False
            if n5 > self.pg_num:
                self.pg_num_rarr = []
                n1 = self.pg_num + 1
                while n1 <= n5:
                    self.pg_num_rarr.append(n1)
                    n1+= 1
            else: self.pg_num_rarr = False

            self.bilds = []
            i = 1
            n_first = 0 if self.num_pages == 0 else (self.pg_num-1) * bilds_in_seite
            n1 = n_first+bilds_in_seite
            bs = bs [n_first:n1]
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

    def get_context_data(self, **kwargs):
        context = super(OneImageView, self).get_context_data(**kwargs)
        context['aurl'] = self.request.build_absolute_uri()
        curr_bild = context [self.context_object_name]
        qs = get_sort_bilds_list (curr_bild.seite)
        ind = 0
        while qs[ind].pk <> curr_bild.pk: ind+= 1
        qs_len = qs.count()
        if ind==0:
            pg = 1 + (qs_len-1) / bilds_in_seite
            context['prev_bild'] = '../../'+str(pg)+'/'+str(qs[qs_len-1].pk)
            context['prev_titel'] = qs[qs_len-1].titel
        else:
            pg = 1 + (ind-1) / bilds_in_seite
            context['prev_bild'] = '../../'+str(pg)+'/'+str(qs[ind-1].pk)
            context['prev_titel'] = qs[ind-1].titel

        if ind>=qs_len-1:
            pg = 1
            context ['next_bild'] = '../../'+str(pg)+'/'+str(qs[0].pk)
            context ['next_titel'] = qs[0].titel
        else:
            pg = 1 + (ind+1) / bilds_in_seite
            context ['next_bild'] = '../../'+str(pg)+'/'+str(qs[ind+1].pk)
            context ['next_titel'] = qs[ind+1].titel
        return context

    def dispatch(self, request, *args, **kwargs):
        self.pg_num = kwargs['pg_num']
        return DetailView.dispatch(self, request, *args, **kwargs)