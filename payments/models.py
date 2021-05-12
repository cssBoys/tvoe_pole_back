import uuid

from django.db import models
from django.db.models.signals import post_save

from payments.signals import post_payment_success


class Payments(models.Model):   
    class Status(models.IntegerChoices):
        FAIL = 0
        PENDING = 1
        SUCCESS = 2
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to="account.CustomUser", on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)

    class Meta:
        verbose_name = "Пополнения"
        verbose_name_plural = "Пополнения"


post_save.connect(post_payment_success, sender=Payments)