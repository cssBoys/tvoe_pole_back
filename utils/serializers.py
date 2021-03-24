from rest_framework import serializers
from .models import DayOfWeek, City

class DayOfWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = DayOfWeek
        fields = ["id", "title"]


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ["id", "title"]
