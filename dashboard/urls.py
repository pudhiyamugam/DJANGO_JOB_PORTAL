from django.urls import path
from . import views

urlpatterns=[
    path("",views.dashboard,name="dashboard"),
    path("job_seeker/",views.job_seeker_dashboard, name="job_seeker_dashboard"),
    path("recruiter/",views.recruiter_dashboard,name="recruiter_dashboard"),
]