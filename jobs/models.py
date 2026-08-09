from django.db import models

class Job(models.Model):
    title=models.CharField(max_length=200)
    company=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.IntegerField()
    descritpion=models.TextField()

    def __str__(self):
        return self.title
