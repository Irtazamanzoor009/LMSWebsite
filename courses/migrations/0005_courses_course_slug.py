# Generated by Django 5.0.6 on 2024-06-16 10:01

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_courseinclude_courses_courseincludes'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='courseName', unique=True),
        ),
    ]
