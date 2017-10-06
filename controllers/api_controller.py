import json
from urllib.request import urlopen

from driveshark.configuration import API

class APIController():
	"""
	The APIController allows components to interact with API endpoints
	"""

	# Google Maps API endpoints
	endpoint_geocode = 'https://maps.googleapis.com/maps/api/geocode/json'
	endpoint_distance = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric'

	def get_place_id(self, location):
		"""
		Retreive a place_id from Google Maps API
		:param location: the location data
		:return: the place_id if this place exists and False if it does not
		"""

		# Replace spaces in location data with '+'
		req_addr = location['address'].replace(" ", "+")
		req_city = location['city'].replace(" ", "+")
		req_prov = location['province'].replace(" ", "+")

		# Build query to send to maps API
		params = '?address=' + req_addr + ',' + req_city + ',' + req_prov + '&key='
		query = self.endpoint_geocode + params + API['GOOGLE_MAPS_KEY']

		# Get coordinates from maps API using urllib2
		# and convert from str to json
		google_response = json.loads(urlopen(query).read())

		# Extract place_id from response
		place_id = [key['place_id'] for key in google_response['results']]

		if len(place_id) == 0: # Invalid place
			return False
		else:
			return place_id[0]

	def get_travel_time(self, origin, destination):
		"""
		Get the travel time between 2 locations
		:param origin: The place_id of the starting point
		:param destination: The place_id of the destination
		:return: The travel time (in mins)
		"""

		# Build query to send to Google
		params = '&origins=place_id:' + origin + '&destinations=place_id:' + destination + '&key='
		query = self.endpoint_distance + params + API['GOOGLE_MAPS_KEY']

		# Get travel time from maps API using urllib2
		# and convert from str to json
		google_response = json.loads(urlopen(query).read())

		# Extract travel time from response
		travel_time = [key['elements'][0]['duration']['text'] for key in google_response['rows']]
		return travel_time[0]
