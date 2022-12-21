from rest_framework.serializers import ModelSerializer
from Brands.models import Brand, BrandCategories
from Products.serializers import ProductSerializer


class BrandCategorySerializer(ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = BrandCategories
        fields = "__all__"


class BrandSerializer(ModelSerializer):
    category = BrandCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = "__all__"