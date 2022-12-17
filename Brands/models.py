from django.db import models
import  os

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(null=True, upload_to='./images/brand')
    image = models.ImageField(null=True, upload_to='./images/brand')


    def img_delete(self, image, thumbnail, *args, **kwargs):
        if os.path.isfile(image):
            img_path = os.path.join('...', image)
            os.remove(img_path)
        if os.path.isfile(thumbnail):
            img_path = os.path.join('...', thumbnail)
            os.remove(img_path)

    def __str__(self):
        return self.name


class BrandCategories(models.Model):
    name = models.CharField(max_length=200, null=True)
    brands = models.ForeignKey(Brand, related_name='category', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name