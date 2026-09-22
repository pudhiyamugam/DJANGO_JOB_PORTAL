from django.db import models
from django.contrib.auth.models import User
import os

class Job(models.Model):
    title=models.CharField(max_length=200)
    company=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.IntegerField()
    descritpion=models.TextField()

    recruiter=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="jobs",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

class Resume(models.Model):

    RESUME_TYPE=[
        ("python","python developer"),
        ("java","java developer"),
        ("web","web developement"),
        ("cyber","cybersecurity"),
        ("mobile","app development")
    ]

    resume_type=models.CharField(
        max_length=50,
        choices=RESUME_TYPE
    )

    applicant=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="resumes"
    )
    file=models.FileField(
        upload_to="resumes/"
    )
    uploaded_at=models.DateTimeField(
        auto_now_add=True
    )

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return f"{self.applicant.username} - {self.resume_type}"

class Application(models.Model):

    job=models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    applicant=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    applied_at=models.DateTimeField(
        auto_now_add=True
    )

    STATUS_CHOICES=[
        ("Applied", "Applied"),
        ("Shortlisted", "Shortlisted"),
        ("Interview", "Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected")
    ]

    status=models.CharField(
        max_length=20,
        default="applied",
        choices=STATUS_CHOICES
    )

    resume = models.ForeignKey(
        Resume,
        on_delete=models.PROTECT,
        related_name="applications",
        null=True,
        blank=True
)

    class Meta:

        constraints=[
            models.UniqueConstraint(
                fields=["job","applicant"],
                name="unique_job_applicant"
            )
        ]

    def __str__(self):
        return f"{self.applicant.username} {self.job.title}"
