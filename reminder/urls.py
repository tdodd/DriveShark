from django.conf.urls import url

from . import views

urlpatterns = [

   # GET /reminders
   url(r'^$', views.get_reminders, name='reminder_list'),

   # POST /reminder
   url(r'^create_trip$', views.create_reminder, name='create_reminder'),

   # DELETE /reminder/{id}
   url(r'^delete_trip/([0-9]+)$', views.delete_reminder, name='delete_reminder'),

]
