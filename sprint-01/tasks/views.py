from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from tasks.forms import NewTaskForm, EditTaskForm, EditSharedTaskForm
from tasks.models import Task
from annoying.decorators import render_to


@render_to('tasks/list.html')
@login_required
def task_list(request):
	user = request.user
	tasks = Task.objects.exclude(is_done=True).filter(
		Q(created_by=user) | Q(collaborators__id=user.id)
	)

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
			new_task = form.save(commit=False)
			new_task.created_by = request.user
			new_task.save()
			form.save_m2m()
			messages.success(request, "Task \"{0}\" created.".format(new_task))
			return redirect(reverse('task_list'))

	return {
		'form': form,
	}


@render_to()
@login_required
def task_edit(request, task_id):
	task = get_object_or_404(Task, pk=task_id)

	if task.created_by == request.user:
		form_name = EditTaskForm
		template = 'tasks/edit.html'
	elif request.user in task.collaborators.all():
		form_name = EditSharedTaskForm
		template = 'tasks/edit_shared.html'
	else:
		raise Http404

	form = form_name(instance=task)

	if request.method == 'POST':
		form = form_name(request.POST, instance=task)
		if form.is_valid():
			form.save()
			messages.success(request, "Task \"{0}\" updated.".format(task))
			return redirect(reverse('task_list'))

	return {
		'form': form,
		'TEMPLATE': template,
	}