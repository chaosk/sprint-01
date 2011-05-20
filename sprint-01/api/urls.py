from django.conf.urls.defaults import patterns, url
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
from api.handlers import TaskHandler
from lib.piston_utils import Resource

auth = HttpBasicAuthentication(realm="HTTP Basic")
task_resource = Resource(TaskHandler, authentication=auth)

# 1st revision of API
urlpatterns = patterns('',
	url(r'^1/tasks/$', task_resource,
		name='api_tasks_list'),

	# automated documentation
	url(r'^1/docs/$', documentation_view, name='api_docs'),
)
