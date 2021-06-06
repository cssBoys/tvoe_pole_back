from playground.models import Playground
from django.db import models
from rest_framework import serializers
from booking.models import Booking
from booking.exceptions import NotEnoughtBalanceException


class BookingSerializer(serializers.ModelSerializer):

    date_start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    date_finish = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    read_only_fields = ('user',)

    class Meta:
        model = Booking
        fields = ["playground", "date_start", "date_finish"]


    def create(self, validated_data):
        from account.models import CustomUser
        from playground.models import Playground

        user = validated_data.get('user')
        playground = Playground.objects.get(id=validated_data.get('playground'))

        if user.balance < playground.price:
            raise NotEnoughtBalanceException

        user.balance -= playground.price
        user.save()

        return super().create(validated_data)