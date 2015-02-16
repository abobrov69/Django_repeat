from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
#        kwargs ['path'] = [v for k,v in self.request.META.items() if k == 'PATH_INFO'][0]
        return super(AboutView,self).get_context_data(**kwargs)
