from django.http import Http404

from ..models import Job
from .technology_service import list_technologies_id


def list_jobs():
    jobs = Job.objects.all()
    return jobs


def insert_jobs(job):
    job_db = Job.objects.create(title=job.title, description=job.description, salary=job.salary,
                                company_name=job.company_name, amount_of_jobs=job.amount_of_jobs,
                                contact=job.contact, type_of_job=job.type_of_job)
    job_db.save()
    for i in job.technologies:
        tech = list_technologies_id(i.id)
        job_db.technologies.add(tech)

    return job_db


def list_jobs_id(id):
    try:
        return Job.objects.get(id=id)
    except Job.DoesNotExist:
        raise Http404


def update_jobs(job_before_update, new_job):
    job_before_update.title = new_job.title
    job_before_update.description = new_job.description
    job_before_update.salary = new_job.salary
    job_before_update.company_name = new_job.company_name
    job_before_update.amount_of_jobs = new_job.amount_of_jobs
    job_before_update.contact = new_job.contact
    job_before_update.type_of_job = new_job.type_of_job
    job_before_update.technologies.set(new_job.technologies)
    job_before_update.save(force_update=True)


def remove_jobs(job):
    job.delete()
