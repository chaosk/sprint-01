from django import forms
from tasks.models import Task


class NewTaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('title', 'description', 'priority',
			'due_to', 'collaborators')


class EditTaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('title', 'description', 'priority',
			'due_to', 'collaborators', 'is_done')

class EditSharedTaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('is_done',)
