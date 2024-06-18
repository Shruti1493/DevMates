# Generated by Django 4.2.6 on 2024-06-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_is_staff_alter_userprofile_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='college',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='end_year',
            field=models.DateField(blank=True, help_text='Optional. End Year', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='start_year',
            field=models.DateField(blank=True, help_text='Optional.Start year', null=True),
        ),
    ]