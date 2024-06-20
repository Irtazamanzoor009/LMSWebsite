# Generated by Django 5.0.6 on 2024-06-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageSubHeadingsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details_subHeadingIcon', models.FileField(default=None, max_length=250, null=True, upload_to='aboutpage/')),
                ('details_subHeading', models.CharField(max_length=50)),
                ('details_subHeadingContent', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutpagedetails',
            name='details_subHeading1',
        ),
        migrations.RemoveField(
            model_name='aboutpagedetails',
            name='details_subHeading2',
        ),
        migrations.RemoveField(
            model_name='aboutpagedetails',
            name='details_subHeadingContent1',
        ),
        migrations.RemoveField(
            model_name='aboutpagedetails',
            name='details_subHeadingContent2',
        ),
        migrations.RemoveField(
            model_name='aboutpagedetails',
            name='details_subHeadingIcon1',
        ),
        migrations.RemoveField(
            model_name='aboutpagedetails',
            name='details_subHeadingIcon2',
        ),
    ]
