from django.db import models

# Create your models here.

class JYLiu_CV(models.Model):
	cv = models.FileField(null=True, blank=True,upload_to='cv/');

	class Meta:
		verbose_name = 'JYLiu CV'
		verbose_name_plural = 'JYLiu CV'

class Member(models.Model):
	english = models.CharField(max_length=30)
	chinese = models.CharField(max_length=10)
#	thumb = models.ImageField(upload_to = 'member_thumbnails/', default = 'member_thumbnails/member_thumb.png')
	thumb = models.FileField(blank=True, upload_to='paper/', default='member_thumbnails/member_thumb.png');
	IDENTITY = (
		('PD','Postdoctoral'),
		('FA','Full-time Assistant'),
		('PS','PhD Student'),
		('MS','Master Studnet'),
	)
	identity = models.CharField(
		max_length=2,
		choices=IDENTITY,
		default='PD',
	)

	email  = models.EmailField(max_length=100)

	class Meta:
		ordering = ['english']

	def __str__(self):
		return self.english


class Past(models.Model):
	english = models.CharField(max_length=30)
	chinese = models.CharField(max_length=10)
	nation  = models.CharField(max_length=15)
	start   = models.DateField()
	end	  = models.DateField()

	IDENTITY = (
		('VP','Visiting Proffesor'),
		('PD','Postdoctoral'),
	)

	identity = models.CharField(
		max_length=2,
		choices=IDENTITY,
		default='VP',
	)

	class Meta:
		ordering = ['-end']

	def __str__(self):
		return self.english

class Graduate(models.Model):
	chinese = models.CharField(max_length=10)
	start   = models.DateField()
	end	  = models.DateField()
	title	  = models.CharField(max_length=200)

	IDENTITY = (
		('PD','Philosophiæ Doctor'),
		('MD','Master'),
	)

	identity = models.CharField(
		max_length=2,
		choices=IDENTITY,
		default='PD',
	)

	class Meta:
		ordering = ['-end']

	def __str__(self):
		return self.chinese
