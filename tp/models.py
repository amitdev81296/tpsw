from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from datetime import date


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
    user = models.OneToOneField(User, unique=True)
    student_id = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(default=timezone.now)
    profile_photo = models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/photos_folder', max_length=100)
    resume_pdf = models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/resumes_folder', max_length=100)
    marksheet_pdf = models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/marksheets_folder', max_length=100)
    document_pdf = models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/documents_folder', max_length=100)
    do_you_have_plans_for_higher_studies = models.BooleanField()
    where_do_you_see_yourself_in_the_coming_two_years = models.TextField(max_length=300)
    why_did_you_choose_engineering = models.TextField(max_length=300)
    allowed = models.BooleanField()

    def get_age(self):
        today = date.today()
        dob = self.birth_date
        return int(today.year) - int(dob.year)
