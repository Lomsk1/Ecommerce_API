from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = "__all__"
        # fields = ['id', 'email', 'first_name', 'last_name', 'password']


# class ProductWishlistSerializer(ModelSerializer):
#     wishlist = WishlistSerializer(many=True, read_only=True)
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'wishlist']

# class CurrentUserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'is_staff')