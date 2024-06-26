# Generated by Django 5.0.1 on 2024-03-28 20:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=500)),
                ('event_description', models.TextField(blank=True, max_length=500, null=True)),
                ('permission_type', models.CharField(choices=[('IO', 'Invitation only'), ('CO', 'Club members only'), ('P', 'Public')], max_length=500)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('repetition_type', models.CharField(choices=[('NR', 'Not repeated'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], max_length=500)),
                ('repetition_length', models.IntegerField(blank=True, null=True)),
                ('is_IRL', models.BooleanField()),
                ('location', models.TextField(blank=True, null=True)),
                ('location_link', models.URLField(blank=True, null=True)),
                ('event_link', models.URLField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('parent_club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_club', to='clubs.club')),
            ],
        ),
    ]
