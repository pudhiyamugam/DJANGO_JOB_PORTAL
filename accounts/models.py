from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    ROLE_CHOICES=[("job_seeker","job seeker"),("recruiter","recruiter")]

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    role=models.CharField(max_length=20,choices=ROLE_CHOICES)

    is_profile_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class RecruiterProfile(models.Model):

    profile=models.OneToOneField(
        Profile,
        on_delete=models.CASCADE
    )

    company_name=models.CharField(max_length=200)
    company_location=models.CharField(max_length=200)
    company_website=models.URLField(blank=True)
    company_description=models.TextField()

    def __str__(self):
        return self.company_name

class  JobSeekerProfile(models.Model):

    profile=models.OneToOneField(
        Profile,
        on_delete=models.CASCADE
    )

    phone=models.CharField(max_length=10)
    education=models.TextField()
    skill=models.TextField()
    resume=models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.profile.user.username

# Create your models here.
