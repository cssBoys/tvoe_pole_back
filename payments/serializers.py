import uuid
from rest_framework import serializers
from payments import (models, exceptions, paybox)
from rest_framework import status


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payments
        fields = ['amount', ]


    def create(self, validated_data):
        order_id = str(uuid.uuid4())
        amount = validated_data.get('amount')
        validated_data['order_id'] = order_id
        paybox_payment = paybox.Payment()
        result, status_code = paybox_payment.run(order_id, amount)
        if status_code != status.HTTP_201_CREATED:
            raise exceptions.PaymentSerivceNotAnswer
        self.payment_url = result.get('payment_page_url')
        instance = models.Payments.objects.create(**validated_data)
        return instance

    @property
    def data(self):
        result = super().data
        result['payment_url'] = self.payment_url
        return serializers.ReturnDict(result, serializer=self)