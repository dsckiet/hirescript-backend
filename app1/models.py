from django.db import models
from django import validators

# models here !
class company(models.Model):
	name = models.CharField(max_length='30')
	website = models.UrlField(blank=True)
	link = models.UrlField()

	def __str__(self):
		return name
	
class job(model.Model):
	profile=models.CharField()
	companies=models.ManytoManyField(company)
	founded = models.DateField()
	location = models.CharField(max_length='100')
	emp_count = models.IntegerField()
	description = models.TextField(max_length='300')
	job_category = models.TextField()
	tags = models.TextField()
	job_info = models.TextField(blank=True)
	experience = models.IntegerField(blank=True)

	def __str__(self):
		return profile

