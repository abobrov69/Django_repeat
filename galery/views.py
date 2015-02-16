from django.views.generic import TemplateView, ListView
from models import GalerieSeite

class AuthorView(TemplateView):
    template_name = "author.html"
    def get_context_data(self, **kwargs):
#        kwargs ['path'] = [v for k,v in self.request.META.items() if k == 'PATH_INFO'][0]
        return super(AuthorView,self).get_context_data(**kwargs)

class PageListView(ListView):
    model = GalerieSeite
    template_name = "pages_list.html"
    context_object_name = 'seite_liste'
