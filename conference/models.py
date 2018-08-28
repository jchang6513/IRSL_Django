from django.db import models

# Create your models here.

class Conference(models.Model):
	start = models.DateField()
	end   = models.DateField()
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200)

	class Meta:
		ordering = ['-start','-end']

	def __str__(self):
		return self.title

class Oral(models.Model):
	date  = models.DateField()
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200)

	class Meta:
		ordering = ['-date']
	
	def __str__(self):
		return self.title
