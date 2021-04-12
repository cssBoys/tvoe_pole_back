from django.core.cache import cache


def post_user_save(instance, sender, created, **kwargs):
    if created:
        cache.set(str(instance.id), '7777', 60 * 3)
