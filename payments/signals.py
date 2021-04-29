
def post_payment_success(instance, sender, created, **kwargs):
    if instance.status == instance.Status.SUCCESS:
        user = instance.user
        user.balance += instance.amount
        user.save()
