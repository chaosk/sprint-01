from django.contrib.auth.decorators import login_required
from django.db.models import Q
from tasks.models import Task
from annoying.decorators import render_to


@render_to('tasks/list.html')
@login_required
def task_list(request):
	user = request.user
	tasks = Task.objects.filter(Q(created_by=user) | Q(collaborators__id=user))

	return {
		'tasks': tasks,
	}
