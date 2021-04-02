from .models import Article, ArticleImage
from .serializers import ArticleListSerializer,  ArticleDetailSerializer ,ImageListSerializer

from rest_framework.permissions import AllowAny
from rest_framework import generics


from . import serializers
from utils.pagination import CustomPageNumberPagination
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets




'''
class ArticleList(generics.ListCreateAPIView):
	#permission_classes = (permissions.IsAuthenticated,) #method1

	queryset = Article.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = (permissions.IsAuthenticated,) #method1
	
	queryset = Article.objects.all()
	permission_classes = (AllowAny,) # method3
	serializer_class = ArticleDetailSerializer
'''


class ArticleViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = serializers.ArticleListSerializer
    serializer_action_classes = {
        'list': serializers.ArticleListSerializer,
        'retrieve': serializers.ArticleDetailSerializer
    }
    queryset = Article.objects.all().order_by('-date')
    permission_classes = (AllowAny, )
    pagination_class = CustomPageNumberPagination


    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
           return super().get_serializer_class()



class ImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ImageListSerializer    






