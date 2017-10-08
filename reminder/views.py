from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Reminder

def get_reminders(request):
	"""
	Get the list of reminders
	"""
	return render(request, 'components/reminders.html', { 'reminder_list': Reminder.objects.all() })

def create_reminder(request):
	"""
	Create a new reminder
	"""
	try:
		# Create reminder with request data
		Reminder(
			trip=request.POST['trip_id'],
			reminder_time=request.POST['reminder_time'],
		).save()

		# Redirect to reminders page with confirmation
		messages.success(request, 'Reminder added')
		return redirect('/reminders')
	except:
		messages.error(request, 'Could not create reminder')
		return redirect('/reminders')


def delete_reminder(request, reminder_id):
	"""
	Delete a reminder
	:param reminder_id: the id of the reminder to delete
	"""
	if request.POST['_method'] == 'DELETE':
		Reminder.objects.filter(id=request.POST['_id']).delete()

		# Redirect to reminders page with confirmation
		messages.success(request, 'Reminder deleted')
		return redirect('/reminders')
