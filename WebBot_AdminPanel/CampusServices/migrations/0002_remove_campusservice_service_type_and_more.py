# Generated by Django 4.2.19 on 2025-03-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CampusServices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campusservice',
            name='service_type',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.AddField(
            model_name='campusservice',
            name='service',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CampusServices.service'),
        ),
    ]
