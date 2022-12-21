from django.db import models
import os
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='./category', null=True)

    def img_delete(self, image, *args, **kwargs):
        if os.path.isfile(image):
            img_path = os.path.join('...', image)
            os.remove(img_path)

    def __str__(self):
        return self.title