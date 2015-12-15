#from django.shortcuts import render_to_response, render
from sys import exc_info
from forms import MsgForm2
from models import Publication
from datetime import datetime
from django.views.generic import RedirectView, TemplateView, ListView
from django.views.generic.list import MultipleObjectMixin # , View, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from django.contrib.auth.models import AnonymousUser
from django.views.generic.detail import DetailView
from PIL import Image as PILImage
from mysite.settings import MEDIA_URL
from mysite.functions import get_absolute_root_url

news_url_page_pref = '/nachrichten'
small_image_width = 350.0
small_image_height = 280.0



def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

class MsgListView(ListView):
    model = Publication
    template_name = "publication_list.html"
    context_object_name = 'messages_list'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MsgListView,self).dispatch (request, *args, **kwargs)

class BlogMainMixin (object):
    paginate_by = 10
    model = Publication
    queryset = Publication._default_manager.filter (isdeleted=False)

"""
    def get_queryset (self):
        if self.queryset is not None:
            queryset = self.queryset
            if hasattr(queryset, '_clone'):
                queryset = queryset._clone()
        elif self.model is not None:
            queryset = self.model._default_manager.filter (isdeleted=False)
        else:
            raise ImproperlyConfigured("'%s' must define 'queryset' or 'model'"
                                       % self.__class__.__name__)
        return queryset
"""

class BlogMainView(BlogMainMixin,ListView):
#    form_class = MsgForm
    context_object_name = 'msg_list'
    show_msg_lenght = 120
    db_error = False
    form = False
    template_name = 'blog.html'
    url_prefix = news_url_page_pref
    max_page_list_lenght = 10
    min_page_list_lenght = 5


    def dispatch(self, request, *args, **kwargs):
        self.hostname = request.get_host()
        return ListView.dispatch(self, request, *args, **kwargs)

    def get_template_names(self):
        return [self.template_name]

    def get_queryset (self):

#        queryset = BlogMainMixin.get_queryset(self)
        queryset = super (BlogMainView, self).get_queryset()
        for msg in queryset:
                if len(msg.text) > self.show_msg_lenght: msg.text = msg.text[:self.show_msg_lenght-5] + ' ...'
        return queryset

#    def render_to_response(self, context, **response_kwargs):
#        a = dc
#        return super (BlogMainView,self).render_to_response(self, context, **response_kwargs)


    def get_context_data(self, **kwargs):
        context = super(BlogMainView, self).get_context_data(**kwargs)
#        q1 = context.__class__.__name__
#        bbb = qqq
        context ['db_error'] = self.db_error
        if self.form: context['form'] = self.form
        context['url_prefix'] = ""
        if self.url_prefix: context['url_prefix'] = self.url_prefix
        if self.hostname: context['hostname'] = self.hostname
        page_list_lenght = min (self.max_page_list_lenght, context ['paginator'].num_pages / 2 + 1)
        page_list_lenght = max (page_list_lenght, min (self.min_page_list_lenght, context ['paginator'].num_pages ))
        if page_list_lenght >= context ['paginator'].num_pages:
            start = 0
            end = context ['paginator'].num_pages
        elif context ['page_obj'].number <= page_list_lenght / 2 + 1:
            start = 0
            end = page_list_lenght
        elif context ['page_obj'].number > context ['paginator'].num_pages - page_list_lenght / 2:
            end = context ['paginator'].num_pages
            start = end - page_list_lenght
        else:
           start =  context ['page_obj'].number - page_list_lenght / 2 - 1
           end = start + page_list_lenght

        context ['left_dots'] = ' '+str (start)+' ' if start>0 else ''
        context ['right_dots'] = ' '+str(end + 1)+' ' if end<context ['paginator'].num_pages else ''
        context ['pg_list'] = [' '+str(x+1)+' ' for x in range (start, end) ]
        context ['page_txt'] = context ['page_obj'].__repr__()[5:-1]
#        aaa = bbb
        return context

#    def SetFormUser (self,request):
#        self.form.user = '' if request.user.is_anonymous() else request.user.username
#        u = self.form.user
#        asdqd = asdasdasdsd

    def get(self, request, *args, **kwargs):
        initial = None
        if 'request_POST' in request.session:
            initial = {}
            initial['message'] = request.session ['request_POST']['message']
            del request.session["request_POST"]
#            eff = dfsdfsf
#        self.form = self.form_class(initial=initial)
#        self.SetFormUser (request)
#        c = kwargs ['context']
#        aaaa = ldfkldfk
        return super(BlogMainView, self).get (request)

"""
    @method_decorator(gns_login_required)
    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST)
#        self.SetFormUser (request)
#        context = {'form': self.form}
#        ib = request.session['requst_POST']
#        aaaaaaaaaa = ffffffffff
        if self.form.is_valid():
            cd = self.form.cleaned_data
            self.db_error = False
            try:
                Publication (date=datetime.now(), text=cd['message'], author=request.user).save()
                # form = MsgForm()
            except DatabaseError:
                self.form = self.form_class(request.POST)
                self.db_error = exc_info()[1].message
                return super(BlogMainView, self).get (request)  #  self.render_to_response(self.get_context_data(context)) #
            return HttpResponseRedirect (reverse('blogclass'))
        return super(BlogMainView, self).get (request)  #  self.render_to_response(self.get_context_data(context))
"""

class BlogMainViewAnchor(BlogMainMixin,MultipleObjectMixin,RedirectView):

    def get_redirect_url(self, **kwargs):
        post = self.kwargs.get('post') or self.request.GET.get('post')
#        aaa = bbbqew
        redir_str = news_url_page_pref + '/'
        try:
            post = int(post)
        except ValueError:
            aaa = bbb
            return redir_str
        qs = self.get_queryset ()
        i = 0
        l = len (qs)
        if l % self.paginate_by == 0:
            z = (l-1)/self.paginate_by
        else: z = l/self.paginate_by
#        bbb = kjhkjh
        for i in range (z):
            if qs [(i+1)*self.paginate_by].pk<post:
                start = i*self.paginate_by
                end = (i+1)*self.paginate_by
                break
        else:
            i += 1
            start = i*self.paginate_by
            end = len(qs)
        if end > start:
            for j in range (start,end):
                if qs[j].pk == post:
                    redir_str += (str (i+1) + "/#" + str(post))
                    z = qs[j].isdeleted
                    break
            else:
                redir_str += str (i+1)
#        aaa = asdasd
        return redir_str

"""
    def get (self, request, *args, **kwargs):
        post = self.kwargs.get('post') or self.request.GET.get('post')
        redir_str = '/'
        try:
            post = int(post)
        except ValueError:
            self.url = redir_str
            return HttpResponseRedirect (redir_str)
        qs = self.get_queryset ()
        for i in range (len(qs)/self.paginate_by):
            if qs [(i+1)*self.paginate_by].pk<post:
                start = i*self.paginate_by
                end = (i+1)*self.paginate_by
                break
        else:
            i += 1
            start = i*self.paginate_by
            end = len(qs)
        if end > start:
            for j in range (start,end):
                if qs[j].pk == post:
                    redir_str += (str (i+1) + "/#" + str(post))
                    z = qs[j].isdeleted
#                    bbb = kjhkjh
                    break
            else:
                redir_str += str (i+1)
#                aaa = asdasd
        self.url = redir_str
        return HttpResponseRedirect (redir_str)
"""

class CheckDeletedMsgMixin (object):
    model = Publication

    def get (self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.isdeleted:
           return HttpResponseRedirect ('/'+'/post'+str(obj.pk))
        else:
            return self.upper_class.get (self, request, *args, **kwargs)

class MakeSuccessUrlMixin (CheckDeletedMsgMixin):
    error_template_name = "publication_user_error.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if (not request.user.username) or request.user.username <> obj.author.username:
            self.template_name = self.error_template_name
            self.success_url = '/'
        else: self.success_url = reverse_lazy('msg_post', args=[str(obj.pk)])
        return self.upper_class.dispatch(self, request, *args, **kwargs)

class MsgDelete(MakeSuccessUrlMixin,DeleteView):
    success_url = reverse_lazy('blogclass')
    template_name = "publication_confirm_delete.html"
    upper_class = DeleteView

class MsgView (CheckDeletedMsgMixin,DetailView):
    template_name = "publication_detail.html"
    upper_class = DetailView
    default_image = 'portrait.jpg'

    def get_context_data(self, **kwargs):
        context = self.upper_class.get_context_data(self,**kwargs)
        context['aurl'] = self.request.build_absolute_uri()
        queryset = self.model._default_manager.filter (isdeleted=False)
        pk_current = context['object'].pk
        pk_prev = -1
        pk_next = -1
        l = len(queryset)
        for i in range(0,l-1):
            if queryset[i].pk > pk_current:
               pk_next = queryset[i].pk
               context ['next_titel']= queryset[i].titel
               context ['next_date']= queryset[i].date
            else: break
        if l==1:
            i=1
        else:
            i = i+1
        if i<l:
            pk_prev = queryset[i].pk
            context ['prev_titel']= queryset[i].titel
            context ['prev_date']= queryset[i].date
        context ['next_pk'] = pk_next
        context ['prev_pk'] = pk_prev
        i = context['object'].img_klein.name
        if i: context ['kl_img'] = i.strip()
        else: context ['kl_img'] = self.default_image
        i = get_absolute_root_url(context['aurl'])+MEDIA_URL
        context ['kl_img'] = i + context ['kl_img']
        return context


def ImageResize (img_gr, width, height):
    if width > height:
        kf = width / small_image_width
        if height / kf > small_image_height: kf = height / small_image_height
    else: kf = height / small_image_height
    return img_gr.resize((int(width/kf),int(height/kf)),PILImage.ANTIALIAS)


class MsgFormSaveMixin (object):
    form_class = MsgForm2

    def form_valid(self, form):
        if self.create:
            form.instance.date = datetime.now()
            form.instance.author = self.request.user
        self.object = form.save()
        if form.instance.img_gross:
            if form.instance.img_gross.name [0:2] == './': form.instance.img_gross.name = form.instance.img_gross.name [2:]
            img_gr = PILImage.open(form.instance.img_gross.path)
            img_kl = ImageResize(img_gr, form.instance.img_gross.width, form.instance.img_gross.height )
            form.instance.img_klein.name = 'kl_'+form.instance.img_gross.name
            img_kl.save (form.instance.img_klein.path)
#        aaaa = bbb
        return self.upper_class.form_valid(self,form)

class MsgUpdate(MakeSuccessUrlMixin,MsgFormSaveMixin,UpdateView):
    success_url = reverse_lazy('blogclass')
    template_name = "publication_form.html"
    upper_class = UpdateView
    create = False

class MsgCreate (MsgFormSaveMixin,CreateView):
    template_name = "publication_form.html"
    model = Publication
    success_url = reverse_lazy('blogclass')
    upper_class = CreateView
    create = True

    def dispatch(self, request, *args, **kwargs):
        if not request.user.username:
            self.template_name = "publication_user_error.html"
            self.success_url = '/'
        return self.upper_class.dispatch(self, request, *args, **kwargs)

