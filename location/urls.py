from django.conf.urls import url

from . import views

urlpatterns = [

	# GET /
	url(r'^$', views.LocationListView.as_view(), name='location_list'),

	# POST /
	url(r'^create_location$', views.create_location, name='create_location'),

	# DELETE /
	url(r'^delete_location/([0-9]+)$', views.delete_location, name='delete_location'),

]
