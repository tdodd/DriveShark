from django.conf.urls import url

from . import views

urlpatterns = [

   # GET /reminders
   url(r'^$', views.get_reminders, name='reminder_list'),

   # POST /reminders
   url(r'^create_reminder$', views.create_reminder, name='create_reminder'),

   # DELETE /delete_reminder/{id}
   url(r'^delete_reminder/([0-9]+)$', views.delete_reminder, name='delete_reminder'),

]
