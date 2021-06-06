from django.db import models


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    day = models.ManyToManyField(to='utils.DayOfWeek')
    playground = models.ForeignKey(to='playground.Playground', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to="account.CustomUser", on_delete=models.CASCADE, null=True)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
