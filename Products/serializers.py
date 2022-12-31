from rest_framework.serializers import ModelSerializer
from Products.models import Product, ProductImages, ProductBranch, Specifications, \
    SpecificationBasics
from Branch.serializers import BranchSerializer


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductBranchSerializer(ModelSerializer):
    # branch = BranchSerializer(many=True, read_only=True)
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
    branch = SpecificationsSerializer(many=True, read_only=True)
    specification = ProductBranchSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"