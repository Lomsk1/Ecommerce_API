from rest_framework.serializers import ModelSerializer
from Category.models import Category
from Products.serializers import ProductSerializer


class CategorySerializer(ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
