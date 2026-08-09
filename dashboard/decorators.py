from functools import wraps
from django.shortcuts import redirect

def recruiter_required(view_function):

    @wraps(view_function)
    def wrapper(request, *args, **kwargs):

        if request.user.profile.role!="recruiter":

            return redirect("dashboard")

        return view_function(request, *args, **kwargs)

    return wrapper


def jobseeker_required(view_function):

    @wraps(view_function)
    def wrapper(request, *args, **kwargs):

        if request.user.profile.role!="job_seeker":
            return redirect("dashboard")

        return view_function(request, *args, **kwargs)

    return wrapper