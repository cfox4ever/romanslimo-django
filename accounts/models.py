from django.db import models
from simple_history.models import HistoricalRecords
# from .setups import STATES, ChoiceRole

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import PermissionsMixin

from django.utils import timezone
from crum import get_current_request,  get_current_user
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=20, blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    contact_no = models.CharField(max_length=80, blank=True)
    role = models.ManyToManyField(Roles)
    
    history = HistoricalRecords()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return (self.username)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def save(self, *args, **kwargs):
        username = self.first_name + ' ' + self.last_name
        self.username = username

        super(CustomUser, self).save(*args, **kwargs)