from datetime import datetime

from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Reminder
from trip.models import Trip

def get_reminders(request):
	"""
	Get the list of reminders
	"""
	context = {
		'reminder_list': Reminder.objects.all(),
		'trip_list': Trip.objects.all(),
	}
	return render(request, 'components/reminders.html', context)

def create_reminder(request):
	"""
	Create a new reminder
	"""
	try:
		# Remove spaces input and format time
		time = request.POST['reminder_time'].replace(' ', '')
		time = datetime.strptime(time, '%I:%M%p')

		# Get associated trip
		trip = Trip.objects.get(id=request.POST['trip_id'])

		# Create reminder
		Reminder(
			trip=trip,
			reminder_time=time,
		).save()

		# Redirect to reminders page with confirmation
		messages.success(request, 'Reminder added')
		return redirect('/reminders')
	except:
		messages.error(request, 'Invalid time format')
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
