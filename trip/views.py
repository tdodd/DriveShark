from django.shortcuts import render

def trip_listview(request):
	"""
	/trips listview
	"""
	return render(request, 'components/trips.html')
