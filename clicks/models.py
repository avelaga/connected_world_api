from django.db import models

class Click(models.Model):
  date = models.DateField(auto_now=True)
  time = models.TimeField(auto_now=True)
  x = models.IntegerField()
  y = models.IntegerField()
  hue = models.IntegerField()
