from .utils import generate_code

def post_user_save(instance, sender, created, **kwargs):
    if created:
        generate_code(instance.id, instance.phone)
 