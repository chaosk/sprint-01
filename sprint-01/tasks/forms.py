from django import forms
from tasks.models import Task


class NewTaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('title', 'description', 'priority',
			'due_to', 'collaborators')
