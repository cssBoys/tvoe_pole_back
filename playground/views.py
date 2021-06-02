from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated


from utils.pagination import CustomPageNumberPagination
from .models import Category, Playground, Review
from . import serializers

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes

import playground


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny, )



class PlaygroundViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.PlaygroundListSerializer
    serializer_action_classes = {
        'list': serializers.PlaygroundListSerializer,
        'retrieve': serializers.PlaygroundDetailsSerializer
    }
    queryset = Playground.objects.all()
    permission_classes = (AllowAny, )
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    @action(detail=True, permission_classes=[IsAuthenticated, ], methods=['get', ])
    def watch(self, request, pk):
        from booking.models import Booking
        day = request.query_params.get('day')
        playground = Playground.objects.get(id=pk)
        data = [
            {
                'hour': hour,
                'active': True
            } for hour in range(
                playground.time_start.hour, 
                playground.time_finish.hour
            )
        ]
        booking_qs = Booking.objects.filter(playground_id=pk, day=day)
        for booking in booking_qs:
            for el in data:
                for hour in range(booking.time_start.hour, booking.time_finish.hour):
                    if el['hour'] == hour:
                        el['active'] = False
        return Response(data)
        

    



class ReviewCreateViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = serializers.ReviewCreateSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
