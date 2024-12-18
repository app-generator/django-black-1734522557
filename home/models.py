# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Positions(models.Model):

    #__Positions_FIELDS__
    entry_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    exit_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    symbol = models.TextField(max_length=255, null=True, blank=True)
    order_type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    lot_size = models.IntegerField(null=True, blank=True)

    #__Positions_FIELDS__END

    class Meta:
        verbose_name        = _("Positions")
        verbose_name_plural = _("Positions")



#__MODELS__END
