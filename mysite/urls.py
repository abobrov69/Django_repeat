from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import AboutView, RootPageView
from galery.views import AuthorView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^ueber/$', AboutView.as_view()),
    (r'^kunstler/$', AuthorView.as_view()),
    url(r'^galerie/', include('galery.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    (r'(^([^/]+)/)*$', RootPageView.as_view()),

)
