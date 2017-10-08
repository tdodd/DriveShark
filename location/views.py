from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView

from location.models import Location
from controllers.api_controller import APIController

class LocationListView(ListView):
	"""
	Homepage location list
	"""
	model = Location
	template_name = 'components/locations.html'

def create_location(request):
	"""
	Create a new location
	"""

	# Get place id
	p_id = APIController().get_place_id(request.POST)

	if not p_id: # Invalid place
		messages.error(request, 'Invalid Location')
		return redirect('/')
	else:
		# Create new place
		Location(
			alias = request.POST['alias'],
			address = request.POST['address'],
			city = request.POST['city'],
			province = request.POST['province'],
			place_id = p_id
		).save()

		# Redirect to homepage with confirmation
		messages.success(request, 'Location added')
		return redirect('/')


def delete_location(request, location_id):
	"""
	Delete a location
	"""
	if request.POST['_method'] == 'DELETE':
		Location.objects.filter(id=request.POST['_id']).delete()

		# Redirect to homepage with confirmation
		messages.success(request, 'Location deleted')
		return redirect('/')
