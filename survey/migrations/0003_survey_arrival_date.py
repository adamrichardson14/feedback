# Generated by Django 2.1.3 on 2018-11-14 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_survey_date_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='arrival_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]