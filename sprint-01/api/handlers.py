from django.contrib.auth.models import User
from django.db.models import Q
from tasks.models import Task
from piston.handler import BaseHandler


class TaskHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = Task
	fields = ('id', 'title', 'created_at', 'created_by',
		'due_to', 'description', 'is_done',  ('collaborators', ()))

	@classmethod
	def resource_uri(cls, task=None):
		task_id = 'id'
		if task:
			task_id = task.id
			return ('api_tasks_detail', [task_id])


	def read(self, request, *args, **kwargs):
		"""
		URL
			**/api/1/tasks/**
		Shortdesc
			Returns a list of unfinished tasks.
		Arguments
			- none
		Data
			- none
		Result
			- 200 - when everything went fine
				list of Task objects
		"""
		user = request.user
		return Task.objects.exclude(is_done=True).filter(
			Q(created_by=user) | Q(collaborators__id=user.id)
		)


class UserHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('id', 'username', 'get_full_name')
	model = User
