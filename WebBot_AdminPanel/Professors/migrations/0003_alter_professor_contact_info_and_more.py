# Generated by Django 4.2.19 on 2025-03-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Professors', '0002_alter_professor_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='contact_info',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='full_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='linked_in',
            field=models.URLField(blank=True, max_length=255, unique=True),
        ),
    ]
