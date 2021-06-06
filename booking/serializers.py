from django.db import models
from rest_framework import serializers
from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):

    date_start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    date_finish = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Booking
        fields = ["playground", "date_start", "date_finish"]
