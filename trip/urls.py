from django.conf.urls import url

from . import views

urlpatterns = [

   # GET /trips
   url(r'^$', views.get_trips, name='trip_list'),

	# POST /trip
	url(r'^create_trip$', views.create_trip, name='create_trip'),

	# DELETE /trip/{id}
	url(r'^delete_trip/([0-9]+)$', views.delete_trip, name='delete_trip'),

]
