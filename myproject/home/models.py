from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    answer = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
