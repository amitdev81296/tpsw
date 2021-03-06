from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from datetime import date
from django.core.validators import MinValueValidator


class UserSignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {'password': forms.PasswordInput}


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
    BRANCH_CHOICES = (
        ('IT', 'IT'),
        ('MECH', 'MECH'),
        ('COMPS', 'COMPS'),
        ('ITI', 'ITI'),
        ('HM', 'HM'),
    )
    user = models.OneToOneField(User, unique=True)
    student_id = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(default=timezone.now)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    cgpa = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0.01)])
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

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.TextField(max_length=100)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
