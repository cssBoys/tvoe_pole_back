from rest_framework import serializers
from .models import Article, ArticleImage


class ArticleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Article
		fields = ["id","title", "cover","date","address"]


	




class ArticleImageSerializer(serializers.ModelSerializer):

	class Meta:
		model = ArticleImage
		fields = ["image"]







class ArticleDetailSerializer(serializers.ModelSerializer):

	#imageSet = serializers.RelatedField(source='image', read_only=True)

	class Meta:
		model = Article
		fields = ["id","title","cover","body","date","address"]

