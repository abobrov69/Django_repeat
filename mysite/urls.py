from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import AboutView, RootPageView, ImageCreateView, NewsCreaView
from galery.views import AuthorView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^ueber/$', AboutView.as_view()),
    (r'^kunstler/$', AuthorView.as_view()),
    url(r'^galerie/', include('galery.urls')),
    url(r'^nachrichten/', include('nachrichten.urls')),
    url(r'^macht/', include(admin.site.urls)),
    url(r'^image_create/$', ImageCreateView.as_view(), name='image_edit'),
    url(r'^news_create/$', NewsCreaView.as_view(), name='news_edit'),
    url('^$', RootPageView.as_view (), name="rootpage"),
)
