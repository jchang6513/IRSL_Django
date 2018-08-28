from django.db import models

# Create your models here.

class Publication_List(models.Model):
	List = models.FileField(null=True, blank=True,upload_to='paper/');
	
	class Meta:
		verbose_name = 'Publications List'
		verbose_name_plural = 'Publications List'

class International(models.Model):
	NO = models.BigIntegerField();
	author = models.TextField(blank=True);
	title = models.TextField(blank=True);
	paper = models.FileField(null=True, blank=True,upload_to='paper/');

	class Meta:
		ordering = ['-NO']

	def __str__(self):
		return str(self.NO)
	
class Domestic(models.Model):
	NO = models.BigIntegerField();
	author = models.TextField(blank=True);
	title = models.TextField(blank=True);
	paper = models.FileField(null=True, blank=True,upload_to='paper/');

	class Meta:
		ordering = ['-NO']
	
	def __str__(self):
		return str(self.NO)
    
class Book(models.Model):
	NO = models.BigIntegerField();
	author = models.TextField(blank=True);
	title = models.TextField(blank=True);
	paper = models.FileField(null=True, blank=True,upload_to='paper/');

	class Meta:
		ordering = ['-NO']
	
	def __str__(self):
		return str(self.NO)
