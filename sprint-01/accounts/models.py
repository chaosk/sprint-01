from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True, related_name='profile')

	class Meta:
		get_latest_by = 'user__created_at'
		ordering = ['id']

	def __unicode__(self):
		possessive = '' if self.user.username.endswith('s') else 's'
		return u"{0}'{1} profile".format(self.user.username, possessive)

	def get_absolute_url(self):
		return self.user.get_absolute_url()


def post_user_save(instance, **kwargs):
	if kwargs['created']:
		profile = UserProfile(
			user=instance,
		)
		profile.save()

post_save.connect(post_user_save, sender=User,
	dispatch_uid='accounts.models')
