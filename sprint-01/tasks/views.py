from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from tasks.forms import NewTaskForm
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


@render_to('tasks/add.html')
@login_required
def task_add(request):
	form = NewTaskForm()

	if request.method == 'POST':
		form = NewTaskForm(request.POST)
		if form.is_valid():
			new_task = form.save()
			messages.success(request, "Task \"{0}\" created.".format(new_task))
			return redirect(reverse('task_list'))

	return {
		'form': form,
	}