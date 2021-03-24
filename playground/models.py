from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)


class PlaygroundType(models.Model):
    title = models.CharField(max_length=255)



class Playground(models.Model):
    # LOGICAL FIELDS
    title = models.CharField(max_length=255)
    time_start = models.TimeField()
    time_finish = models.TimeField()
    categories = models.ManyToManyField(to='Category')
    working_days = models.ManyToManyField(to='utils.DayOfWeek')
    city = models.ForeignKey(to='utils.City', on_delete=models.CASCADE)
    price = models.FloatField()

    # ADDITIONAL FIELDS
    phone = models.CharField(max_length=255)
    playground_type = models.ForeignKey(
        to='PlaygroundType',
        on_delete=models.SET_NULL,
        null=True
    )
    address = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
