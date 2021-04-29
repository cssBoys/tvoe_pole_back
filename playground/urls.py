from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PlaygroundViewSet , ReviewCreateViewSet

router = DefaultRouter()

router.register("category", CategoryViewSet, basename="category")
router.register("playground", PlaygroundViewSet, basename="playground")
router.register("review", ReviewCreateViewSet, basename="review")

urlpatterns = router.urls
