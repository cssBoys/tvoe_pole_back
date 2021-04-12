from rest_framework import serializers
from .models import Article, ArticleImage


class ArticleListSerilaizer(serializers.ModelSerializer):

	class Meta:
		model = Article
		fields = ["id", "title", "date", "main_image"]


class ImageListSerializer(serializers.ModelSerializer):

	image = serializers.SerializerMethodField()

	def get_image(self, obj):
		return obj.image.url

	class Meta:
		model = ArticleImage
		fields = ["image"]


class ArticleDetailSerializer(serializers.ModelSerializer):

	images = ImageListSerializer(read_only=True, many=True)
	
	class Meta:
		model = Article
		fields = ["id","title","body","date","images"]










	