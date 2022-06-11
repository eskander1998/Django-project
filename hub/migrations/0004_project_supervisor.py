# Generated by Django 3.2 on 2022-02-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_project_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_coach', to='hub.coach'),
        ),
    ]