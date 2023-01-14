from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from Products.serializers import ProductSerializer
from rest_framework.serializers import ModelSerializer


import Products.serializers

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = "__all__"
        # fields = ['id', 'email', 'first_name', 'last_name', 'password']


# class CurrentUserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'is_staff')