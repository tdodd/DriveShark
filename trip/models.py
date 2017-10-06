from django.db import models

class Trip(models.Model):
	from_pid = models.CharField(max_length=255)
	to_pid = models.CharField(max_length=255)
	from_text = models.CharField(max_length=255)
	to_text = models.CharField(max_length=255)
