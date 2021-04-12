from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=255)

	@property
	def main_image(self):
		if self.images.first():
			return self.images.first().image.url
		return None

	def __str__(self):
		return self.title


class ArticleImage(models.Model):
	article = models.ForeignKey(to="Article", on_delete=models.CASCADE, related_name="images")
	image = models.ImageField()



	

	



















'''
class Contact(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	profile_img = models.ImageField()
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	#user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
'''