# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp', '0003_auto_20170826_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='document_pdf',
            field=models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/documents_folder'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='marksheet_pdf',
            field=models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/marksheets_folder'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/photos_folder'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume_pdf',
            field=models.FileField(upload_to='C:/Users/nijsu/PycharmProjects/tpsw/tp/resumes_folder'),
        ),
    ]
