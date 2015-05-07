from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^create/$', 'api.views.create', name="create"),
    url(r'^oauth2callback/$', 'api.views.auth_return'),
)

