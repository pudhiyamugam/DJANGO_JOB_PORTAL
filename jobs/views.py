from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm
from dashboard.decorators import recruiter_required
from django.contrib.auth.decorators import login_required

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

@login_required
@recruiter_required
def create_job(request):
    if request.method=="POST":
        form=JobForm(request.POST)

        if form.is_valid():
            job=form.save(commit=False)
            job.recruiter=request.user
            job.save()
            return redirect("recruiter_dashboard")
    else:
        form=JobForm()

        context={
            "form":form
        }

    return render(request,"jobs/create_job.html",context)

@login_required
@recruiter_required
def my_jobs(request):
    jobs=request.user.jobs.all()

    return render(request,"jobs/my_jobs.html",{"jobs":jobs})

@login_required
@recruiter_required
def edit_job(request,id):
    job=request.user.jobs.get(id=id)

    if request.method=="POST":
        form=JobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()

            return redirect("my_jobs")

    else:
        form=JobForm(instance=job)

    return render(
        request,
        "jobs/edit_job.html",
        {
            "form":form,
            "job":job
        }
    )
