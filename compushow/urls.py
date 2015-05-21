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

	url(r'^logout/', logout ),

    url(r'^api/get_computistas/', 'compushow_app.views.get_computistas'),
    
    url(r'^api/get_computistas_nombre/', 'compushow_app.views.get_computistas_nombre'),

    url(r'^user/(?P<idU>[\w]+)/$', 'compushow_app.views.welcome', name='bien'),
    
# <<<<<<< HEAD
#     url(r'^(?P<nombre>[\w]+)/$', Nominacion, name='nombre_nominacion'),

#     url(r'^(?P<nombre>[\w]+)/Votar$', Votacion, name='nombre_votacion'),

# =======
    url(r'^user/(?P<idU>[\w]+)/nominacion/(?P<name>[\w]+)/$', nominacion, name='nombre_nominacion'),
# >>>>>>> 4e524352d79d9f0d01d8a5e1dff99d44581a1006
) + static(settings.STATIC_URL,)
