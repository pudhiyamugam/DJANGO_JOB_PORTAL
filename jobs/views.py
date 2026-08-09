from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm

def home(request):

    jobs=Job.objects.all()
    context={
        "jobs":jobs,
        "portal_name":"job portal",
        "username":request.user
    }
    return render(request,"jobs/home.html",context)

def job_details(request,id):

    job=get_object_or_404(Job,id=id)

    context={
        "job":job,
    }

    return render(request,"jobs/job_details.html",context)

def create_job(request):
    if request.method=="POST":
        form=JobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=JobForm()

        context={
            "form":form
        }

    return render(request,"jobs/create_job.html",context)
