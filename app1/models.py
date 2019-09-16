from python import uuid
from django.db import models

# models here !
class job(models.Model):
	company = models.CharField(max_legth='30', default=uuid.uuid4(), primary_key=True)
	profile = models.CharField()
	founded = models.CharField(blank=True)
	location = models.CharField(max_legth='100')
	emp_count = models.IntegerField()
	description = models.TextField(max_legth='300')
	job_CATEGORY = (('F-O','full_time_office')('P-O','part_time_office')('P-H','part_time_home')('I-O','intern_office')('I-H','intern_home'))
	job_category = models.CharField(choice=job_CATEGORY)
    # tags: ["javascript", "angular", "jquery", "nodejs", "reactjs", "mongodb", "vuejs", "sql"]
    website = models.CharField(validators=[validate_url])
    job_info = models.TextField(blank=True)
    link = models.CharField(validators=[validate_url])
    experience = models.IntegerField(blank=True)
