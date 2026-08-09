from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("<int:id>/",views.job_details,name="job_details"),
    path("create/",views.create_job,name="create_job")
]