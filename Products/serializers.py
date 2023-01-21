from rest_framework.serializers import ModelSerializer
from Products.models import Product, ProductImages, ProductBranch, Specifications, \
    SpecificationBasics
from wishlist.serializers import WishlistSerializer

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductBranchSerializer(ModelSerializer):
    class Meta:
        model = ProductBranch
        fields = '__all__'


class SpecificationBasicsSerializer(ModelSerializer):
    class Meta:
        model = SpecificationBasics
        fields = "__all__"


class SpecificationsSerializer(ModelSerializer):
    basic = SpecificationBasicsSerializer(many=True, read_only=True)
    class Meta:
        model = Specifications
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    branch = ProductBranchSerializer(many=True, read_only=True)
    specification = SpecificationsSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"