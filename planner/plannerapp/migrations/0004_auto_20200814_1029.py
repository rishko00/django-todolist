# Generated by Django 3.0.7 on 2020-08-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plannerapp', '0003_auto_20200813_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_end',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_start',
            field=models.TimeField(blank=True),
        ),
    ]