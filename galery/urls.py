from django.conf.urls import patterns, include, url
from galery.views import PageListView, PageView, OneImageView

urlpatterns = patterns('',
    url(r'^$', PageListView.as_view(), name='index'),
    url(r'^image/(?P<pg_num>\d+)/(?P<pk>\d+)/$', OneImageView.as_view(), name='image'),
    url(r'^(?P<seite_url>\w+)/(?P<pg_num>\d+)/$', PageView.as_view(), name='detail'),
    url(r'^(?P<seite_url>\w+)/$', PageView.as_view(), name="detail"),
)