from django.conf.urls import url

from . import views

urlpatterns = [

    # /trips
    url(r'^', views.trip_listview),

]
