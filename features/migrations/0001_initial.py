# Generated by Django 5.0.6 on 2024-06-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featuresIcon', models.CharField(max_length=50)),
                ('featursHeading', models.CharField(max_length=50)),
                ('featuresDescription', models.TextField()),
            ],
        ),
    ]
