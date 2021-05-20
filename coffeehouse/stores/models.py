from django.core.exceptions import ValidationError
from django.db import models

from datetime import date
from django.db.models.fields import CharField, DateField
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=30, null=False, blank=True)
    state = models.CharField(max_length=2, null=False, blank=True)
    email = models.EmailField(null=False, blank=True)
    
    
    class Meta:
        unique_together = ("name", "email")

    # date = models.DateField(default=date.today)
    # datetime = models.DateTimeField(default=timezone.now)
    # date_lastupdated = models.DateField(auto_now=True)
    # date_added = models.DateField(auto_now_add=True)
    # timestamp_lastupdated = models.DateTimeField(auto_now=True)
    # timestamp_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s, %s, %s' % (self.name, self.address, self.city)

    def clean(self):
        if self.city == 'San Diego' and self.state != 'CA':
            raise ValidationError(""" Wait San Diego is CA!, are you sure there is San Diego in %s ?""" % self.state)
