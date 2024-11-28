from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import User_Manager


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    username = None  # Disable the username field
    email = models.EmailField(_("email address"), unique=True)  # Use email as the unique identifier
    USERNAME_FIELD = "email"  # Set email as the USERNAME_FIELD
    REQUIRED_FIELDS = []  # No additional fields are required for creating a user

    # Link the custom manager to the User model
    objects = User_Manager()  # Corrected: Don't pass email and password here

    def __str__(self):
        return self.email
class UserProfile(BaseModel):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(unique=True, max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"