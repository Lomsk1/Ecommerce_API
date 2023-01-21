from django.db import models
from django.contrib.auth import get_user_model
from ecommerceAPI import settings
from Products.models import Product


User = get_user_model()


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wishlist', on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Product, on_delete=models.CASCADE,
                                    related_name='wishlist', null=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.wished_item.title
        return self.wished_item.id