# Generated by Django 2.1.3 on 2018-11-17 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20181117_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='cleanlinesstarget',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='servicetarget',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='tmexceedtarget',
        ),
    ]