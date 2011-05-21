from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	created_by = models.ForeignKey(User, related_name="tasks")
	due_to = models.DateTimeField(blank=True, null=True)
	description = models.TextField(blank=True)
	is_done = models.BooleanField(default=False)
	collaborators = models.ManyToManyField(User, related_name="shared_tasks")

	PRIORITY_VERY_LOW = 1
	PRIORITY_LOW = 2
	PRIORITY_NORMAL = 3
	PRIORITY_HIGH = 4
	PRIORITY_CRITICAL = 5
	PRIORITY_CHOICES = (
		(PRIORITY_VERY_LOW, "Very low"),
		(PRIORITY_LOW, "Low"),
		(PRIORITY_NORMAL, "Normal"),
		(PRIORITY_HIGH, "High"),
		(PRIORITY_CRITICAL, "Critical"),
	)
	priority = models.IntegerField(choices=PRIORITY_CHOICES,
		default=PRIORITY_NORMAL)

	def __unicode__(self):
		return self.title
