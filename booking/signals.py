from account.tasks import send


def notify_client(instance, sender, created, **kwargs):
    if created:
        send.delay(instance.user.phone, "Вы успешно забронировали")
