from django.conf.urls import patterns, include, url
from django.contrib import admin
from galery.views import AboutView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^about/$', AboutView.as_view()),
)
