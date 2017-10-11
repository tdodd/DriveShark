from background_task import background
from django.contrib.auth.models import User

from reminder.models import Reminder

def notify_user():
	"""
	Background job to send notifications to user
	"""

	user = User.objects.get(pk=user_id)
	user.email_user('Here is a notification', 'You have been notified')
