# Generated by Django 2.1.3 on 2018-11-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_survey_sitecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='cleanlinesstarget',
            field=models.IntegerField(default=60.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='servicetarget',
            field=models.IntegerField(default=65.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='tmexceedtarget',
            field=models.IntegerField(default=55.0),
            preserve_default=False,
        ),
    ]
