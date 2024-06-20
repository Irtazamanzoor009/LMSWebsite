# Generated by Django 5.0.6 on 2024-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_courselearn_courses_courselearns'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='courseIncludes',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='courseLearns',
        ),
        migrations.AddField(
            model_name='courses',
            name='CourseOverView',
            field=models.TextField(blank=True, default='default text', null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='courseDesc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='courseInstructor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='courseInstructorJob',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='courseinclude',
            name='courseIncludeIcon',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='courseinclude',
            name='courseIncludecontent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courselearn',
            name='learnContent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
