from django.db import models
from datetime import time

class Campus(models.Model):
   campus_id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)
   pic = models.CharField(max_length=200, default="")

   def __str__(self):
      return self.name

class Restaurant(models.Model):
   restaurant_id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   campus_id = models.ForeignKey(Campus,on_delete = models.CASCADE)
   opening_hours = models.TimeField(default=time(hour=0,minute=0))
   closing_hours = models.TimeField(default=time(hour=0,minute=0))
   capacity = models.IntegerField(default=0)
   staff_only = models.BooleanField(default=False)
   is_open_we = models.BooleanField(default=False)
   we_opening_hours = models.TimeField(default=time(hour=0,minute=0))
   we_closing_hours = models.TimeField(default=time(hour=0,minute=0))
