from django.db import models

class DayOfWeek(models.Model):
    title = models.CharField(max_length=255)

class City(models.Model):
    title = models.CharField(max_length=255)
