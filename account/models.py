from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from account.managers import CustomUserManager
from account.signals import post_user_save


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), unique=True)
    phone = models.CharField(_('Phone'), unique=True, max_length=50)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'name', 'surname']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email


post_save.connect(post_user_save, sender=CustomUser)