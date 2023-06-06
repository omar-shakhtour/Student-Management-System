from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
        label="",
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
        label="",
    )
    major = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Major", "class": "form-control"}
        ),
        label="",
    )
    department = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Department", "class": "form-control"}
        ),
        label="",
    )
    class_level = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Class Level", "class": "form-control"}
        ),
        label="",
    )
    gpa = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "GPA", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        model = Record
        exclude = ("user",)
