from django.db import models
from booking.signals import notify_client
from django.db.models.signals import post_save


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    playground = models.ForeignKey(to='playground.Playground', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to="account.CustomUser", on_delete=models.CASCADE, null=True)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()


post_save.connect(notify_client, sender=Booking)
