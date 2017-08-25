from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput}


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.OneToOneField(User)
    student_id = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    resume_pdf = models.FileField(upload_to='./resumes_folder', max_length=100)
    marksheet_pdf = models.FileField(upload_to='./marksheets_folder', max_length=100)
    document_pdf = models.FileField(upload_to='./documents_folder', max_length=100)
    birth_date = models.DateField(default=timezone.now)
    do_you_have_plans_for_higher_studies = models.BooleanField()
    where_do_you_see_yourself_in_the_coming_two_years = models.TextField(max_length=300)
    why_did_you_choose_engineering = models.TextField(max_length=300)
    allowed = models.BooleanField()
