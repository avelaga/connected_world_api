from django.db import models

class Click(models.Model):
  date = models.CharField(max_length=200, null=True)
  time = models.CharField(max_length=200, null=True)
  x = models.IntegerField()
  y = models.IntegerField()
  hue = models.IntegerField()
