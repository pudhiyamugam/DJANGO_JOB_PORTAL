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

        widgets={

            "title":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"enter the job title"
                }
            ),
            "company":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"enter company name"
                }
            ),
            "location":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"enter job location"
                }
            ),
            "salary":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"enter the salary"
                }
            ),
            "descritpion":forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"description",
                    "rows":5
                }
            )

        }

class ApplicationStatusForm(forms.ModelForm):

    class Meta:
        model=Application
        fields=["status"]

class ResumeForm(forms.ModelForm):

    class Meta:
        model=Resume
        fields=["resume_type","file"]

class ApplicationForm(forms.ModelForm):

    class Meta:
        model=Application
        fields=["resume"]

    def __init__(self,*args,user=None,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["resume"].queryset=user.resumes.all()