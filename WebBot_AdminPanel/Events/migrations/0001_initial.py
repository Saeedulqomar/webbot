# Generated by Django 4.2.19 on 2025-02-19 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=255)),
                ('event_type', models.CharField(choices=[('LECTURE', 'Lecture'), ('WORKSHOP', 'Workshop'), ('EXHIBITION', 'Exhibition')], default='WORKSHOP', max_length=10)),
                ('organized_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='Events.organizer')),
            ],
            options={
                'indexes': [models.Index(fields=['date'], name='Events_even_date_4b5efe_idx')],
            },
        ),
    ]
