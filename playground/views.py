from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny


from utils.pagination import CustomPageNumberPagination
from .models import Category, Playground, Review
from . import serializers

from .serializers import ReviewCreateSerializer, ReviewSerializer


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



class ReviewCreateViewSet(ModelViewSet):
    #permission_classes = (IsAuthorOrReadOnly,)
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.ReviewCreateSerializer
    queryset = Review.objects.all()


    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('I haven\' wrote a review yet.s')