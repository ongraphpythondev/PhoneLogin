from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from phone_field import PhoneField


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone_no, password, **extra_fields):

        if not phone_no:
            raise ValueError('The given phone number must be set')
        user = self.model(phone_no=phone_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_no, password=None, **extra_fields):
        """Create and save a regular User with the given phone_no and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_no, password, **extra_fields)

    def create_superuser(self, phone_no, password, **extra_fields):
        """Create and save a SuperUser with the given phone_no and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_no, password, **extra_fields)



class User(AbstractUser):
    """User model."""

    username = None
    phone_no = PhoneField(unique=True   )

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = []
    objects = UserManager()

