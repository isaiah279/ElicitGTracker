# Generated by Django 4.0.6 on 2023-01-18 09:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oilmodel',
            name='description2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oilmodel',
            name='description3',
            field=models.CharField(default=django.utils.timezone.now, max_length=105),
            preserve_default=False,
        ),
    ]
