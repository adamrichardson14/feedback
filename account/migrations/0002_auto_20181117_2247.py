# Generated by Django 2.1.3 on 2018-11-17 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cleanlinesstarget',
            field=models.IntegerField(default=65),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='servicetarget',
            field=models.IntegerField(default=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='tmexceedtarget',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
