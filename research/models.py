from django.db import models

# Create your models here.

class Organization(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ['name']
	
	def __str__(self):
		return self.name

class Research(models.Model):
	start = models.DateField()
	end   = models.DateField()
	title = models.CharField(max_length=500)
	organization = models.ForeignKey(Organization,on_delete=models.CASCADE, default=1)

	class Meta:
		verbose_name_plural = 'Researches'
		ordering = ['-start','-end']

	def __str__(self):
		return self.title
