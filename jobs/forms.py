from django import forms
from .models import Job, Application, Resume

class JobForm(forms.ModelForm):

    class Meta:
        model=Job
        fields=[
            "title",
            "company",
            "location",
            "salary",
            "descritpion"
        ]

class ApplicationStatusForm(forms.ModelForm):

    class Meta:
        model=Application
        fields=["status"]

class ResumeForm(forms.ModelForm):

    class Meta:
        model=Resume
        fields=["file"]