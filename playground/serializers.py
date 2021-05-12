from rest_framework import serializers
from .models import Category, Playground, PlaygroundImage, Review
from utils.serializers import DayOfWeekSerializer, CitySerializer
from django.contrib.auth.models import User


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"



class PlaygroundListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playground
        fields = ["id", "title", "cover", "address", "price", "rating"]


class CategorySerializer(serializers.ModelSerializer):

    playgrounds = PlaygroundListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", "playgrounds"]


class PlaygroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaygroundImage
        fields = ["image"]


class PlaygroundDetailsSerializer(serializers.ModelSerializer):

    working_days = DayOfWeekSerializer(many=True, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    reviews = ReviewCreateSerializer(many=True)

    class Meta:
        model = Playground
        fields = [
            "id",
            "title",
            "address",
            "time_start",
            "time_finish",
            "working_days",
            "city",
            "price",
            "phone",
            "rating",
            "longitude",
            "latitude",
            "reviews",
        ]
