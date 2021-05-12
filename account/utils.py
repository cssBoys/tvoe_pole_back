import string
from random import choice
from django.core.cache import cache
from .tasks import send


def generate_code(id, phone):
    chars = string.digits
    code = ''.join(choice(chars) for _ in range(4))
    send.delay(phone, code)
    cache.set(str(id), code, 60 * 3)