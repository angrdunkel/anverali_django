from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator, EMPTY_VALUES
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

import re

from .managers import MyUserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    USER_TYPES = (
        (1, 'Administrator'),
        (2, 'Customer'),
        (3, 'Performer'),
    )
    username = models.CharField(
        max_length=15, 
        unique=True,
    )
    email = models.EmailField(
        max_length=30, 
        unique=True
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(
        _('First Name'),
        max_length=128,
        blank=True,
        default=''
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=128,
        blank=True,
        default=''
    )
    middle_name = models.CharField(
        _('Middle name'), max_length=50,
        blank=True, 
        null=True
    )
    type = models.PositiveIntegerField(
        _('Type'), help_text=_('User type'),
        choices=USER_TYPES,
        default=1
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        null=True, 
        blank=True,
        default=timezone.now
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def is_admin(self):
        if self.type == 1:
            return True
        else: 
            return False
    
    def is_customer(self):
        if self.type == 2:
            return True
        else: 
            return False
        
    def is_performer(self):
        if self.type == 3:
            return True
        else: 
            return False

    def __str__(self):
        return self.email
    

    def save(self, *args, **kwargs):
            self.email = self.email.lower()
            return super(User, self).save(*args, **kwargs)
    
    def get_full_name(self):
        middle_name = getattr(self, 'middle_name', '')
        if middle_name is None:
            middle_name = ''
        full_name = "%s %s %s" % (
            self.first_name,
            middle_name,
            self.last_name
        )
        full_name = re.sub(r'\s+', ' ', full_name)
        return full_name.strip()
    

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='u_profile',
        on_delete=models.CASCADE,
    )
    address = models.CharField(
        _('Address'), max_length=256,
        blank=True, 
        null=True
    )
    phone = models.CharField(
        _("Phone number"), max_length=30,
        null=True, blank=True, unique=False,
        validators=[RegexValidator(r'^[\s\d\(\)-]+$')]
    )
    experience = models.IntegerField(
        _("Experience"),
        default=0)

    def save(self, *args, **kwargs):
        if not self.phone is None:
            self.phone = re.sub(
                r'[-\+\(\)]+', '',
                re.sub(r'\s+', '', self.phone)
            )

        super(UserProfile, self).save(*args, **kwargs)