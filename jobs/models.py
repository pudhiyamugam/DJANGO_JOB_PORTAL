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
