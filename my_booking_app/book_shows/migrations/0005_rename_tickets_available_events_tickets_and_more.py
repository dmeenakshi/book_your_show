# Generated by Django 5.1.1 on 2024-09-20 14:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shows', '0004_alter_events_event_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='tickets_available',
            new_name='tickets',
        ),
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_created_at',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='events',
            name='location',
            field=models.CharField(choices=[('Bangalore', 'Blr'), ('Hyderabad', 'Hyd'), ('Pune', 'Pune'), ('Chennai', 'Chen')], max_length=9),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
