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

    # url(r'^$', loginView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login, name='login'),
    
    # (r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

	url(r'^signup$', signup),

	url(r'^logout/', logout),

    url(r'^test$', test),

    url(r'^api/get_computistas/', 'compushow_app.views.get_computistas'),
    
    url(r'^api/get_computistas_nombre/', 'compushow_app.views.get_computistas_nombre'),

    url(r'^user/(?P<idU>[\w]+)/$', 'compushow_app.views.wellcome', name='bien'),
    
    url(r'^user/(?P<idU>[\w]+)/nominacion/(?P<name>[\w]+)/$', nominacion, name='nombre_nominacion'),
) + static(settings.STATIC_URL,)
