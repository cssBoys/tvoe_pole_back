import requests
from django.conf import settings
from celery import shared_task


@shared_task
def send(phone, code):
    url = 'https://smsc.ru/sys/send.php?login=%s&psw=%s&phones=%s&mes=%s' % (
        settings.SMSC_LOGIN,
        settings.SMSC_PASSWORD,
        phone,
        code
    )
    r = requests.get(url, timeout=60)
    return r.content
