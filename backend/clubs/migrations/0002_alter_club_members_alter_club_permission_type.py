# Generated by Django 5.0.1 on 2024-04-16 21:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='club',
            name='permission_type',
            field=models.CharField(choices=[('invite_only', 'Invite only'), ('request_to_join', 'Request to join'), ('public', 'Public')], max_length=500),
        ),
    ]
