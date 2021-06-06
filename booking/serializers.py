from django.db import models
from rest_framework import serializers
from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ["day", "playground", "time_start", "time_finish"]


    def create(self, validated_data):
        pass