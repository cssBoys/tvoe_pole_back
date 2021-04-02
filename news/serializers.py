from rest_framework import serializers
from .models import Article, ArticleImage


class ArticleListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Article
		fields = ["id","title","date",]


class ImageListSerializer(serializers.ModelSerializer):


	class Meta:
		model = ArticleImage
		fields = ["image"]


class ArticleDetailSerializer(serializers.ModelSerializer):


	articleImages = ImageListSerializer(read_only=True, many=True)
	
	class Meta:
		model = Article
		fields = ["id","title","body","date","articleImages"]










	