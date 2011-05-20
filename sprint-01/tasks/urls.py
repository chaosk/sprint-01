from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tasks.views',
	url(r'^$', 'task_list', name='task_list'),
	url(r'^add/$', 'task_add', name='task_add'),
	url(r'^edit/(?P<task_id>\d+)/$', 'task_edit', name='task_edit'),
)
