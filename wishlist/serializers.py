from rest_framework.serializers import ModelSerializer
from wishlist.models import Wishlist


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"