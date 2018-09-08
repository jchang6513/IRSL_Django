from django.db import models

# Create your models here.

class Publication_List(models.Model):
	List = models.FileField(null=True, blank=True,upload_to='paper/');

	class Meta:
		verbose_name = 'Publications List'
		verbose_name_plural = 'Publications List'

class International(models.Model):
	year   = models.IntegerField();
	no     = models.IntegerField();
	author = models.TextField(blank=True);
	title  = models.TextField(blank=True);
	paper  = models.FileField(null=True, blank=True,upload_to='paper/');

	class Meta:
		ordering = ['-no']

	def __str__(self):
		return str(self.no)

class Domestic(models.Model):
	year   = models.IntegerField();
	no     = models.IntegerField();
	author = models.TextField(blank=True);
	title = models.TextField(blank=True);
	paper = models.FileField(null=True, blank=True,upload_to='paper/');

	class Meta:
		ordering = ['-no']

	def __str__(self):
		return str(self.no)

class Book(models.Model):
	year   = models.IntegerField();
	no     = models.IntegerField();
	author = models.TextField(blank=True);
	title = models.TextField(blank=True);
	paper = models.FileField(null=True, blank=True,upload_to='paper/');

	class Meta:
		ordering = ['-no']

	def __str__(self):
		return str(self.no)
