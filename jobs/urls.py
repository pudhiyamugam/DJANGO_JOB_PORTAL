from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("<int:id>/",views.job_details,name="job_details"),
    path("create/",views.create_job,name="create_job"),
    path("my-jobs/",views.my_jobs,name="my_jobs"),
    path("<int:id>/edit/",views.edit_job,name="edit_job"),
    path("<int:id>/delete/",views.delete_job,name="delete_job")
]