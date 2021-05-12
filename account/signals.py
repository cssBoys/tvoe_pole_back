
def post_user_save(instance, sender, created, **kwargs):
    if created:
        from account.utils import generate_code
        generate_code(instance.id, instance.phone)
 