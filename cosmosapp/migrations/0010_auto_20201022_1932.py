# Generated by Django 3.0.5 on 2020-10-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmosapp', '0009_auto_20201022_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prod',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='prod',
            name='creation_dates',
            field=models.DateField(blank=True, null=True),
        ),
    ]
