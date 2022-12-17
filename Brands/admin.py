from django.contrib import admin
from Brands import models

# Register your models here.

admin.site.register(models.Brand)
admin.site.register(models.BrandCategories)