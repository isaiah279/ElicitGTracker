# Generated by Django 4.0.6 on 2023-01-18 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApp', '0002_alter_oilmodel_description2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugsmodels',
            name='description2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drugsmodels',
            name='description3',
            field=models.CharField(default=django.utils.timezone.now, max_length=105),
            preserve_default=False,
        ),
    ]
