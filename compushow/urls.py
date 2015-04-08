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
    url(r'^signup/', signup),
	url(r'^logout/', logout),
    url(r'^CompuChill/',CompuChill),
    url(r'^CompuGordito/',CompuGordito),
    url(r'^CompuProductista/',CompuProductista),
    url(r'^CompuCartoon/',CompuCartoon),
    url(r'^CompuComadre/',CompuComadre),
    url(r'^CompuCompadre/',CompuCompadre),
    url(r'^CompuLove/',CompuLove),
    url(r'^CompuCuchi/',CompuCuchi),
    url(r'^CompuIntenso/',CompuIntenso),
    url(r'^CompuPregunton/',CompuPregunton),
    url(r'^CompuFitness/',CompuFitness),
    url(r'^CompuTeam/',CompuTeam),
    url(r'^CompuMaster/',CompuMaster),
    url(r'^CompuPro/',CompuPro),
    url(r'^CompuPapi/',CompuPapi),
    url(r'^CompuMami/',CompuMami),
) + static(settings.STATIC_URL,)
