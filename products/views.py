from rest_framework import generics, viewsets, authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Product, SelectedProduct
from .serializers import ProductSerializer, ProductSelectSerializer
from django.db.models import Q


class ProductSearchView(generics.ListAPIView):
    """
    A view for searching product by name and description.
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        query = self.request.query_params.get("q", None)
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Product instances.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductSelectView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=ProductSelectSerializer,
    )
    def post(self, request):
        serializer = ProductSelectSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            select = serializer.validated_data['select']
            try:
                product = Product.objects.get(id=product_id)
                if select:
                    selected_product = SelectedProduct.objects.get_or_create(
                        product=product, user=user
                    )
                    return Response({"message": f"Product '{product.id}' {product.name} selected by '{user.id}' {user.username}"},
                                    status=status.HTTP_200_OK)
                else:
                    selected_product = SelectedProduct.objects.filter(
                        product=product, user=user
                    ).delete()
                return Response({"message": f"Product '{product.id}' {product.name} deselected by '{user.id}' {user.username}"}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
