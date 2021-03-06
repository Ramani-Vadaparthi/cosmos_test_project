# Generated by Django 3.0.5 on 2020-10-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmosapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_family', models.CharField(blank=True, max_length=100, null=True)),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('last_updated_by', models.IntegerField(blank=True, null=True)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('enabled_flag', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Productfamily',
                'verbose_name_plural': 'Productfamily',
            },
        ),
    ]
