from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductSearchView, ProductViewSet, ProductSelectView


router = DefaultRouter()
router.register(r"", ProductViewSet, basename='product')
urlpatterns = router.urls
urlpatterns += [
    path("search", ProductSearchView.as_view(), name="product-search"),
    path("select", ProductSelectView.as_view(), name="product-select"),
]
