from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator


class UserProfileManager(BaseUserManager):
    
    def create_user(self, username, email, phone, firstName, lastName, password, **extra_fields ):
        """
        Create and save a user with the given username, email, password and other feilds.

        """
        if not email:
            raise ValueError("User must have an Email feild")

        normalize_email = self.normalize_email(email)


        if not username:
            raise ValueError("User must provide his Username ")

        if not phone:
            raise ValueError("User must provide his phone number ")

        customUser = self.model(username = username, email = email, phone = phone, firstName = firstName, lastName = lastName, **extra_fields)
        customUser.set_password(password)

        customUser.save(using = self._db)
       
        return customUser

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('phone', '')
        extra_fields.setdefault('firstName', '')
        extra_fields.setdefault('lastName', '')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password=password, **extra_fields)


def user_profilephoto_file_path(instance, filename):
    return f'images/profile_photos/{instance.firstName}_{instance.lastName}_{instance.id}/{filename}'

    
    
        
class UserProfile(AbstractBaseUser, PermissionsMixin):
    username_validator = RegexValidator(
        regex=r'^[\w.@+-]+$', 
        message=_("Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True, help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ), validators=[username_validator],error_messages={
            "unique": _("A user with that username already exists."),
        })
    firstName = models.CharField(max_length=150, blank=True)
    lastName = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=10)


    profile_photo = models.ImageField(upload_to=user_profilephoto_file_path, null=True, blank=True)  # New field for profile photo
    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)


    # Education Information
    college = models.CharField(max_length=100, blank=True, null=True)
    Branch = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.DateField(blank=True, null=True, help_text=_("Optional.Start year"))
    end_year = models.DateField(blank=True, null=True, help_text=_("Optional. End Year"))


    aboutme = models.CharField(max_length=200, blank=True, null=True)

    # # Coding profile Links
    leetcode_profile = models.URLField(max_length=1000, blank=True, null=True, help_text=_("Optional. URL of the user's Leetcode profile."))
    Codechef_profile = models.URLField(max_length=1000, blank=True, null=True, help_text=_("Optional. URL of the user's CodeChef profile."))
    CodeForces_profile = models.URLField(max_length=1000, blank=True, null=True, help_text=_("Optional. URL of the user's Codeforces profile."))
    Github_profile = models.URLField(max_length=1000, blank=True, null=True, help_text=_("Optional. URL of the user's Github profile."))
    Linkedin_profile = models.URLField(max_length=1000, blank=True, null=True, help_text=_("Optional. URL of the user's Linkedin_profile."))

    coding_languages = models.TextField(blank=True,  help_text=_("Optional. List of coding languages known by the user."))
    dev_framework = models.TextField(blank=True,  help_text=_("Optional. List of development frameworks known by the user."))
    databases = models.TextField(blank=True, help_text=_("Optional. List of databases known by the user."))
    cloud = models.TextField(blank=True, help_text=_("Optional. List of cloud technologies known by the user."))
    other = models.TextField(blank=True,  help_text=_("Optional. List of Other technologies known by the user."))
   





    objects = UserProfileManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","phone"]


    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.firstName, self.lastName)
        return full_name.strip()

    def __str__(self):
        return (str(self.id) + " - " + self.email + " - " + self.firstName)
    
