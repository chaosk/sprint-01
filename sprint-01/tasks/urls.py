from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tasks.views',
	url(r'^$', 'task_list', name='task_list'),
)
