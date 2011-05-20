from django import forms
from tasks.models import Task


class NewTaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('title', 'description', 'share_with')
