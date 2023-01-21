from django.db import models
from Category.models import Category
from Brands.models import BrandCategories
from Branch.models import Branch
import os


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product',
                                 on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(BrandCategories, related_name='product',
                              on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    separate = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='./products', blank=True)
    amount = models.IntegerField(blank=True, default=1)
    new = models.BooleanField(default=False)
    price = models.IntegerField(null=True)
    total_price = models.IntegerField(default=0)
    sale = models.IntegerField(blank=True, default=0)
    new_price = models.IntegerField(blank=True, default=0)
    total_new_price = models.IntegerField(blank=True, default=0)
    deadline = models.DateField(null=True, blank=True, default="2099-10-10")
    color = models.CharField(max_length=200, null=True)
    product_model = models.CharField(max_length=200, null=True)
    top = models.BooleanField(default=False, blank=True)
    popularity = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    total_in_stock = models.BooleanField(default=True, blank=True)

    def img_delete(self, thumbnail, *args, **kwargs):
        if os.path.isfile(thumbnail):
            img_path = os.path.join('...', thumbnail)
            os.remove(img_path)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    image = models.ImageField(upload_to='./products', null=True)
    product = models.ForeignKey(Product, related_name='images',
                                on_delete=models.CASCADE, null=True)

    def img_delete(self, image, *args, **kwargs):
        if os.path.isfile(image):
            img_path = os.path.join('...', image)
            os.remove(img_path)

    def __str__(self):
        return self.product.title


class Specifications(models.Model):
    category = models.CharField(max_length=200, blank=True)
    product = models.ForeignKey(Product, related_name='specification',
                              on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.product.title}, {self.category}'


class SpecificationBasics(models.Model):
    name = models.CharField(max_length=200, null=True)
    middle = models.CharField(max_length=200, null=True)
    basic = models.ForeignKey(Specifications, related_name='basic',
                              on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.basic.product.title}, {self.basic.category}, {self.name}'


class ProductBranch(models.Model):
    product = models.ForeignKey(Product, related_name='branch',
                                on_delete=models.CASCADE, null=False)
    branch = models.ForeignKey(Branch, related_name='branch',
                               on_delete=models.CASCADE, null=True)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.title}, {self.branch.name}'