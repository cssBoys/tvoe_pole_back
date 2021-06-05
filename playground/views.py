from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny


from utils.pagination import CustomPageNumberPagination
from .models import Category, Playground, Review
from . import serializers

from rest_framework import permissions, status
from rest_framework.response import Response




#new
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from django_filters import rest_framework as filters, CharFilter
from django_property_filter import PropertyNumberFilter, PropertyFilterSet

class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny, )

class PlaygroundFilter(filters.FilterSet, PropertyFilterSet):
    playground_type = CharFilter(field_name='playground_type__title', lookup_expr='icontains')
    price = filters.RangeFilter()
    
    class Meta:
        model = Playground
        fields = ['playground_type', 'price',] 
        property_fields = [
        ('rating', PropertyNumberFilter, ['lt', 'gt']),
        ]


class PlaygroundViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.PlaygroundListSerializer
    serializer_action_classes = {
        'list': serializers.PlaygroundListSerializer,
        'retrieve': serializers.PlaygroundDetailsSerializer
    }
    queryset = Playground.objects.all()
    permission_classes = (AllowAny, )
    pagination_class = CustomPageNumberPagination


    #new
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('title','address')
    ordering_fields = ['price']
    filterset_class = PlaygroundFilter
    


    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()





class ReviewCreateViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = serializers.ReviewCreateSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)