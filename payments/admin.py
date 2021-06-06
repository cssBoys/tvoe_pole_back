from django.contrib import admin
from payments.models import Payments


admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    ...