from rest_framework.serializers import ModelSerializer
from Category.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
