from django.contrib import admin
from Products.models import Product, ProductBranch, ProductImages, \
    Specifications, SpecificationBasics

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductBranch)
admin.site.register(ProductImages)
admin.site.register(Specifications)
admin.site.register(SpecificationBasics)