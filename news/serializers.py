from rest_framework import serializers
from .models import Article, ArticleImage


class ArticleListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Article
		fields = ["id","title","date",]








class ArticleDetailSerializer(serializers.ModelSerializer):

	

	class Meta:
		model = Article
		fields = ["id","title","date","articleImages"]



	