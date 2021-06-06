from django.http import request
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from booking.serializers import BookingSerializer

class BookingViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user.id)