from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):

    ROLE_CHOICES=[
        ("job_seeker","job seeker"),
        ("recruiter","recruiter")
        ]

    email=forms.EmailField(required=True)

    role=forms.ChoiceField(
        choices=ROLE_CHOICES
    )

    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "role",
            "password1",
            "password2"
        ]