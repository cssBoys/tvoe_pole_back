from rest_framework.exceptions import APIException

class NotEnoughtBalanceException(APIException):
    status_code = 406
    default_detail = "Не достаточно средств"
