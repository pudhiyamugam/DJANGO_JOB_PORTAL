from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application
from .forms import JobForm
from dashboard.decorators import recruiter_required, jobseeker_required
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
            return redirect("my_jobs")
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

@login_required
@recruiter_required
def delete_job(request,id):

    job=request.user.jobs.get(id=id)

    if request.method=="POST":
        job.delete()

        return redirect("my_jobs")

    return render(request,"jobs/delete_job.html",{"job":job})

def job_list(request):
    query=request.GET.get("q")

    if query:
        jobs=Job.objects.filter(
            title__icontains=query
        )
    else:
        jobs=Job.objects.all()

    if request.user.is_authenticated:
        applications=Application.objects.filter(
            applicant=request.user
        )

        applied_job_id=set(applications.values_list(
            "job_id",
            flat=True
        ))

    else:
        applied_job_id=[]

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs":jobs,
            "query":query,
            "applied_jobs":applied_job_id
        }
    )

@login_required
@jobseeker_required
def apply_job(request, id):

    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        is_applied=Application.objects.filter(
            job=job,
            applicant=request.user
        ).exists()
        if not is_applied:

            Application.objects.create(
                job=job,
                applicant=request.user
            )

        return redirect("my_applications")

    return redirect("job_list")

@login_required
@jobseeker_required
def my_applications(request):
    application=Application.objects.filter(
        applicant=request.user
    )

    return render(
        request,
        "jobs/my_applications.html",
        {
            "applications":application
        }
    )

@login_required
@recruiter_required
def applicants(request,id):
    applicants=Application.objects.filter(
        job_id=id
    )
    mode=type(applicants)

    return render(request,"jobs/applicants.html",{
        "applicants":applicants,
        "mode":mode
    })
