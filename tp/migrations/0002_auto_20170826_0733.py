# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_photo',
            field=models.FileField(default='photo.jpg', upload_to='.photos_folder'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='document_pdf',
            field=models.FileField(upload_to='.documents_folder'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='marksheet_pdf',
            field=models.FileField(upload_to='.marksheets_folder'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume_pdf',
            field=models.FileField(upload_to='.resumes_folder'),
        ),
    ]
