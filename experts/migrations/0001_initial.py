# Generated by Django 5.0.6 on 2024-06-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertImage', models.FileField(default=None, max_length=250, null=True, upload_to='experts/')),
                ('expertName', models.CharField(max_length=50)),
                ('expertDesc', models.CharField(max_length=50)),
            ],
        ),
    ]
