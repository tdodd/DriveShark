from django.db import models

class Location(models.Model):
	alias = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	province = models.CharField(max_length=30)
	place_id = models.CharField(max_length=255)