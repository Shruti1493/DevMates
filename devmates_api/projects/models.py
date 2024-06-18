from django.db import models
from accounts.models import *
# Create your models here.
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserProjects(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    openRequest = models.BooleanField(default=False)
    projectName = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    TechStack = models.TextField(max_length=100, blank=True, null=True)
    projectLink = models.URLField(max_length=1000, blank=True, null=True, help_text=_("Optional. URL of the user's project host link."))
    GithubLink = models.URLField(max_length=1000, blank=True, null=True, help_text=_("Optional. URL of the user's project code link."))
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, help_text="Comma-separated tags")
    duration_weeks = models.IntegerField(blank=True, null=True, help_text="Estimated duration in weeks")

   

    def __str__(self):
        return self.projectName


def user_projectImage_file_path(instance, filename):
    return f'images/project_images/{instance.firstName}_{instance.lastName}_{instance.id}_{instance.projectName}/{filename}'


class ProjectImage(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4,blank=True)
    project = models.ForeignKey(UserProjects, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_projectImage_file_path)

    def __str__(self):
        return f"Image for {self.project.projectName}"
    

class ProjectCollaborator(models.Model):
    Col_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(UserProjects, on_delete=models.CASCADE)
    User = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    ROLE_CHOICES = [
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('project_manager', 'Project Manager'),
        ('other', 'Other'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer')
    skills = models.TextField(blank=True, help_text="Skills relevant to the project")   
    responsibilities = models.TextField(blank=True, help_text="Responsibilities in the project")
    collaboration_status = models.CharField(max_length=20, blank=True, null=True)



class ProjectRequest(models.Model):
    request_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(UserProjects, related_name='requests', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField(max_length=300, blank=True, null=True, help_text="Optional. Message accompanying the request.")
    date_requested = models.DateTimeField(_("date requested"), default=timezone.now)
    is_accepted = models.BooleanField(default=False)
    is_declined = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)  

    class Meta:
        unique_together = [['project', 'user']]

    def __str__(self):
        return f"Request from {self.user.get_full_name()} for {self.project.projectName}"


    def accept_request(self):
        if not self.is_accepted:
            self.is_accepted = True
            self.is_pending = False
            self.save()

            
            ProjectCollaborator.objects.create(
                project=self.project,
                user=self.user,
                date_joined=timezone.now(),
                collaboration_status="active"  
            )

    def decline_request(self):
        if not self.is_declined:
            self.is_declined = True
            self.is_pending = False
            self.save()


