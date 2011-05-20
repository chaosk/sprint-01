from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, related_name="tasks")
	due_to = models.DateTimeField(blank=True, null=True)
	description = models.TextField(blank=True)
	is_done = models.BooleanField(default=False)
	collaborators = models.ManyToManyField(User, related_name="shared_tasks")

	def __unicode__(self):
		return self.title
