from rest_framework.exceptions import APIException


class PaymentSerivceNotAnswer(APIException):
    status_code = 503
    default_code = "Система оплаты не отвечает, попробуйте по позже"
    default_detail = "Система оплаты не отвечает, попробуйте по позже"