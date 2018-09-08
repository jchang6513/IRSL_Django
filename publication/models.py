from django.db import models

# Create your models here.

class Publication_List(models.Model):
	List = models.FileField(null=True,upload_to='paper/');

	class Meta:
		verbose_name = 'Publications List'
		verbose_name_plural = 'Publications List'

class International(models.Model):
	year   = models.IntegerField(default=9999);
	no     = models.IntegerField(default=999);
	author = models.TextField();
	title  = models.TextField();
	paper  = models.FileField(null=True,upload_to='paper/');

	class Meta:
		ordering = ['-no']

	def __str__(self):
		return str(self.no)

class Domestic(models.Model):
	year   = models.IntegerField(default=9999);
	no     = models.IntegerField(default=999);
	author = models.TextField();
	title = models.TextField();
	paper = models.FileField(null=True,upload_to='paper/');

	class Meta:
		ordering = ['-no']

	def __str__(self):
		return str(self.no)

class Book(models.Model):
	year   = models.IntegerField(default=9999);
	no     = models.IntegerField(default=999);
	author = models.TextField();
	title = models.TextField();
	paper = models.FileField(null=True,upload_to='paper/');

	class Meta:
		ordering = ['-no']

	def __str__(self):
		return str(self.no)
