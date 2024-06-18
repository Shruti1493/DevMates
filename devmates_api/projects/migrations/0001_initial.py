# Generated by Django 4.2.6 on 2024-06-18 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projects.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProjects',
            fields=[
                ('project_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('projectName', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('projectLink', models.URLField(blank=True, help_text="Optional. URL of the user's project host link.", max_length=1000, null=True)),
                ('GithubLink', models.URLField(blank=True, help_text="Optional. URL of the user's project code link.", max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=projects.models.user_projectImage_file_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.userprojects')),
            ],
        ),
    ]
