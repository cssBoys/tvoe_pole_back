from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PlaygroundViewSet

router = DefaultRouter()

router.register("category", CategoryViewSet, basename="category")
router.register("playground", PlaygroundViewSet, basename="playground")

urlpatterns = router.urls
