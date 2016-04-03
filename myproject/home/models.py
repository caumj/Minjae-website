from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('auth.User')
    purpose = models.TextField()
    period = models.TextField()
    schedule = models.TextField()
    email = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField()
