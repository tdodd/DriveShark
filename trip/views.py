from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages

from trip.models import Trip
from location.models import Location

def get_trips(request):
	"""
	Get the list of trips and locations
	"""
	context = {
		'location_list': Location.objects.all(),
		'trip_list': Trip.objects.all()
	}
	return render(request, 'components/trips.html', context)

def create_trip(request):
	"""
	Create a new trip
	"""
	try:
		# Get locations from db
		start = Location.objects.get(alias=request.POST['from'])
		destination = Location.objects.get(alias=request.POST['to'])

		# Create trip
		Trip(
			from_text=start.alias,
			from_pid=start.place_id,
			to_text=destination.alias,
			to_pid=destination.place_id
		).save()

		# Redirect to trips page with confirmation
		messages.success(request, 'Trip added')
		return redirect('/trips')
	except: # Invalid location(s)
		messages.error(request, 'Invalid location(s)')
		return redirect('/trips')

def delete_trip(request, trip_id):
	"""
	Delete a location
	"""
	if request.POST['_method'] == 'DELETE':
		Trip.objects.filter(id=request.POST['_id']).delete()

		# Redirect to trips page with confirmation
		messages.success(request, 'Trip deleted')
		return redirect('/trips')
