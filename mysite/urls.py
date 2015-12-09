from django.contrib import admin
from django.conf.urls import patterns, include, url
from views import AboutView, RootPageView, ImageCreateView, NewsCreate
from galery.views import AuthorView
from nachrichten.views import BlogMainView, BlogMainViewAnchor, MsgDelete, MsgUpdate, MsgView
from django.contrib.auth.views import login, logout

nachrichten_patterns = patterns('',
    url('^$', BlogMainView.as_view (), name="blogclass"),
    url(r'edit/(?P<pk>\d+)/$', MsgUpdate.as_view(), name='msg_update'),
    url(r'delete/(?P<pk>\d+)/$', MsgDelete.as_view(), name='msg_delete'),
    url(r'^details/(?P<pk>\d+)/$', MsgView.as_view(), name='msg_detail'),
    url(r'^notiz/(?P<post>\d+)/$', BlogMainViewAnchor.as_view(),name='msg_post'),
    url(r'(?P<page>\d+)/$', BlogMainView.as_view ()),
    )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^ueber/$', AboutView.as_view()),
    (r'^kunstler/$', AuthorView.as_view()),
    url(r'^galerie/', include('galery.urls')),
    url(r'^nachrichten/', include(nachrichten_patterns)),
    url(r'^macht/', include(admin.site.urls)),
    url(r'^image_create/$', ImageCreateView.as_view(), name='image_edit'),
    url(r'^news_create/$', NewsCreate.as_view(), name='news_edit'),
    url('^$', RootPageView.as_view (), name="rootpage"),
#    (r'^accounts/login/$', login),  #  ),
#    (r'^accounts/logout/$', logout),
)

