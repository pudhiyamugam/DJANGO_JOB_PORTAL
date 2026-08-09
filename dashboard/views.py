from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import jobseeker_required, recruiter_required


@login_required
def dashboard(request):

    profile=request.user.profile

    if profile.role=="job_seeker":
        return redirect("job_seeker_dashboard")

    elif profile.role=="recruiter":
        return redirect("recruiter_dashboard")

    return redirect("home")


@login_required
@jobseeker_required
def job_seeker_dashboard(request):

    return render(request, "dashboard/job_seeker_dashboard.html")

@login_required
@recruiter_required
def recruiter_dashboard(request):

    return render(request, "dashboard/recruiter_dashboard.html")
# Create your views here.
