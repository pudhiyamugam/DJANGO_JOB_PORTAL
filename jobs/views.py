from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application, Resume
from .forms import JobForm, ApplicationStatusForm, ResumeForm, ApplicationForm
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

    if Application.objects.filter(
        job=job,
        applicant=request.user
    ).exists():
        return redirect("my_applications")

    if request.method == "GET":
        form=ApplicationForm(
            user=request.user
        )

        return render(
            request,
            "jobs/apply_job.html",
                {
                "form":form,
                "job":job
                })

    if request.method == "POST":
        form=ApplicationForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():
            application=form.save(commit=False)
            application.job=job
            application.applicant=request.user
            application.status="Applied"
            application.save()

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
    job=request.user.jobs.get(id=id)
    applicantion_object=job.applications.all()

    form=ApplicationStatusForm()

    return render(request,"jobs/applicants.html",{
        "applications":applicantion_object,
        "job":job,
        "form":form
    })

@login_required
@jobseeker_required
def delete_application(request,id):
    if request.method=="POST":
        (request.user.applications.get(job_id=id)).delete()
        return redirect("my_applications")

    return redirect("my_applications")

@login_required
@recruiter_required
def update_application(request, id):
    application=get_object_or_404(
        Application,
        id=id,
        job__recruiter=request.user
    )
    if request.method=="POST":

        form=ApplicationStatusForm(request.POST,instance=application)
        if form.is_valid():
            form.save()

    return redirect("applicants",application.job.id)

@login_required
@jobseeker_required
def upload_resume(request):

    if request.method == "POST":

        print("FILES:", request.FILES)
        print("POST:", request.POST)

        if request.user.resumes.count() >= 3:
            print("USER ALREADY HAS 3 RESUMES")
            return redirect("my_resumes")

        form = ResumeForm(
            request.POST,
            request.FILES
        )

        print("FORM VALID:", form.is_valid())
        print("FORM ERRORS:", form.errors)

        if form.is_valid():

            resume = form.save(commit=False)
            resume.applicant = request.user
            resume.save()

            print("RESUME SAVED:", resume)

            return redirect("my_resumes")

    else:
        form = ResumeForm()

    return render(
        request,
        "jobs/upload_resume.html",
        {"form": form}
    )

@login_required
@jobseeker_required
def resumes(request):
    resumes=request.user.resumes.all()

    return render(
        request,
        "jobs/resumes.html/",
        {
            "resumes":resumes
        }
    )