from django.db import models
from datetime import datetime

class Profile(models.Model):
    likes = models.IntegerField(default=0)
    friends = models.IntegerField(default=0)
    events = models.IntegerField(default=0)
