# Generated by Django 4.2.6 on 2024-06-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprojects',
            name='TechStack',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
