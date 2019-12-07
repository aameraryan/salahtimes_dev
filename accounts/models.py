from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager
from .validators import phone_validator
from localities.models import Area


class User(AbstractBaseUser, PermissionsMixin):

    preferred_areas = models.ManyToManyField(Area)

    phone = models.CharField(max_length=13, validators=[phone_validator, MinLengthValidator(limit_value=13)], unique=True)
    email = models.EmailField(blank=True, null=True)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_display_name(self):
        return self.first_name
