from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Helper class for Django to work with our custom user model
    """

    def create_user(self, email, name, password=None):
        """
        Creates a new user profile object
        """

        # empty email checks
        if not email:
            raise ValueError("Email address needed")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)     # will store it in a hashed form
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Creates a new superuser with the given details
        """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represent a user's profile inside our system
    """

    # These are the fields of our UserProfile
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # is_active & is_staff are required when we override Django User model
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    # we only hv name in required fields, since email is already required for username
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to obtain user's full name"""

        return self.name

    def get_short_name(self):
        """Used to obtain user's short name"""

        # returns the same as get_full_name, snice we only hv 1 name field
        return self.name

    def __str__(self):
        """To convert the object to a string"""

        return self.email       # since this is unique


class ProfileFeedItem(models.Model):
    """Profile status update"""

    # On delete cascade means that if we delete the User Profile,
    # automatically delete the profile feeds corresponding to that user
    user_profile = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    status_text = models.CharField(max_length=50)
    # automatically create time to now, if date isn't specified
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""

        return self.status_text
