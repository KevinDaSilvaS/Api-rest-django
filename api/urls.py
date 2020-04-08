
from django.urls import path, include

from api.myviews import technology_view, job_view, user_view


urlpatterns = [
    path('technologies/', technology_view.TechnologyList.as_view(), name='tech-list'),
    path('technologies/<int:id>', technology_view.TechnologyListDetail.as_view(), name='tech-list-id'),
    path('jobs/', job_view.JobList.as_view(), name='job-list'),
    path('jobs/<int:id>', job_view.JobListDetail.as_view(), name='job-list-id'),
    path('users/', user_view.UserList.as_view(), name='user-list'),
]