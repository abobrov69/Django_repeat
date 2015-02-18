from django.conf.urls import patterns, include, url
from galery.views import PageListView, MsgView


urlpatterns = patterns('',
    url(r'^$', PageListView.as_view(), name='index'),
    url(r'^(?P<seite_url>\w+)/$', MsgView.as_view(), name='detail'),
)