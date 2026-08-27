from django.db import models
from django.contrib.auth.models import User

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

    status=models.CharField(
        max_length=20,
        default="applied"
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
