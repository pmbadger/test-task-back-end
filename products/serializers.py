from rest_framework import serializers
from .models import Product, SelectedProduct


class ProductSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "selected"]

    def get_selected(self, obj):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            return SelectedProduct.objects.filter(user=user, product=obj).exists()
        else:
            return False


class ProductSelectSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    select = serializers.BooleanField()
