from django.conf.urls.defaults import patterns, url, include, handler404, handler500
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'direct_to_template',
		{'template': 'static/home.html'}, name='home'),
	(r'^', include('accounts.urls')),
)