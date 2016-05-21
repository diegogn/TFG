from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Audits.views.index', name='index'),
    url(r'^audits/', include('Audits.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'welcome.html'}, name='logout'),
    url(r'^signin/$', 'Audits.views.crear_usuario', name='signin'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^documents/$', 'Audits.views.documents', name='documents'),
    url(r'^api/', include('api.urls')),
    url(r'^soc/', include("social.apps.django_app.urls", namespace="social"))
    )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}, name='download'))
