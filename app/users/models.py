from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .managers import CustomAccountManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Account(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_('email address'), unique=True)
  last_name = models.CharField(max_length=150, blank=True)
  first_name = models.CharField(max_length=150, blank=True)
  start_date = models.DateTimeField(default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)

  objects = CustomAccountManager()

  USERNAME_FIELD = 'email'
  #REQUIRED_FIELDS = ['user_name', 'first_name']

  def __str__(self):
    return self.email

