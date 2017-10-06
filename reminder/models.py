from django.db import models
from trip.models import Trip

class Reminder(models.Model):
	trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
	reminder_time = models.TimeField()
