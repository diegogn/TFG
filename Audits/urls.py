from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Test.views.home', name='home'),
    url(r'^uploads/$', 'Audits.views.upload_file', name="uploads"),
    url(r'^questions/$','Audits.views.questions', name="questions"),
    url(r'^questions/create/$','Audits.views.question_create', name="question_create"),
    url(r'^(?P<question_id>\d+)/details/$', 'Audits.views.details', name="details"),
)
