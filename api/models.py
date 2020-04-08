from django.db import models


# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Job(models.Model):
    OPTIONS_JOB = [
        ('fixed', 'Work routine will be mostly done in office or company headquarters'),
        ('remote', 'Work routine will be mostly done home-office ')
    ]

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    salary = models.FloatField(null=True, blank=False)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    amount_of_jobs = models.IntegerField(null=False, blank=False)
    contact = models.EmailField(null=False, blank=False)
    type_of_job = models.CharField(max_length=10, choices=OPTIONS_JOB, null=False, blank=False)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title