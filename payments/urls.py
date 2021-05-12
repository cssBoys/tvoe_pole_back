from django.urls import path, include
from rest_framework import routers
from payments import views

router = routers.DefaultRouter()
router.register('payment', views.PaymentView, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path("payments/<int:order_id>/", views.get_payment),
    path("callback/payment/success/", views.payment_success_webhook, name="paybox-success"),
    path("callback/payment/check/", views.payment_check_webhook, name="paybox-check"),
    path("callback/payment/result/", views.payment_result_webhook, name="paybox-result"),
    path("callback/payment/failure/", views.payment_failure_webhook, name="paybox-failure"),
    path("callback/payment/back/", views.back_callback, name="paybox-back"),
    path("callback/payment/post/", views.post_callback, name="paybox-post"),
]
