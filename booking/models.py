from django.db import models


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    day = models.ManyToManyField(to='utils.DayOfWeek')
    playground = models.ForeignKey(to='playground.Playground')
    user = models.ForeignKey(to="account.CustomUser")
    time_start = models.TimeField()
    time_finish = models.TimeField()

