from django.db import models

class User(models.Model):
  likes = models.IntegerField(default=0)
  
