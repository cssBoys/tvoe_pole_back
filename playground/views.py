from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny


from utils.pagination import CustomPageNumberPagination
from .models import Category, Playground, Review
from . import serializers

from rest_framework import permissions, status
from rest_framework.response import Response


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

    



class ReviewCreateViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = serializers.ReviewCreateSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
