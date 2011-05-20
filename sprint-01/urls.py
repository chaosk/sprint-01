from django.conf.urls.defaults import patterns, url, include, handler404, handler500
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'django.views.generic.simple.direct_to_template',
		{'template': 'static/home.html'}, name='home'),
	(r'^', include('accounts.urls')),
	(r'^tasks/', include('tasks.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)