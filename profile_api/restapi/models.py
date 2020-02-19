from django.db import models

class Profile(models.Model):
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  phone = models.IntegerField()

  def __str__(self):
    return self.name
