from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ItemViewSet, ComboViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"items", ItemViewSet)
router.register(r"combos", ComboViewSet)

urlpatterns = router.urls
