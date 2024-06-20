# Generated by Django 5.0.6 on 2024-06-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details_heading', models.CharField(max_length=50)),
                ('details_content', models.CharField(max_length=100)),
                ('details_subHeadingIcon1', models.FileField(default=None, max_length=250, null=True, upload_to='aboutpage/')),
                ('details_subHeading1', models.CharField(max_length=50)),
                ('details_subHeadingContent1', models.CharField(max_length=100)),
                ('details_subHeadingIcon2', models.FileField(default=None, max_length=250, null=True, upload_to='aboutpage/')),
                ('details_subHeading2', models.CharField(max_length=50)),
                ('details_subHeadingContent2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AboutPageTrustedBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trustedByIcon', models.FileField(default=None, max_length=250, null=True, upload_to='aboutpage/')),
            ],
        ),
    ]