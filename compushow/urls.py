from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from compushow import settings

from django.contrib import admin
from compushow_app.views import *



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compushow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login),
	url(r'^signup$', signup),
	url(r'^logout$', logout),
) + static(settings.STATIC_URL,)
