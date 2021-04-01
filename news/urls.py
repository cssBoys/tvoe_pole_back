from django.urls import path
#from .views import  ArticleList, ArticleDetail

from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ArticleViewSet

'''
urlpatterns = [
    path('<int:pk>/', ArticleDetail.as_view()),
    path('', ArticleList.as_view()),
]
'''


router = DefaultRouter()

router.register("article", ArticleViewSet, basename="article")


urlpatterns = router.urls
