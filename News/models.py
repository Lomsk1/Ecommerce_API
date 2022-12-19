from django.db import models
import os

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='./images/news', blank=True)
    deadline = models.DateTimeField(null=True)

    def img_delete(self, image, *args, **kwargs):
        if os.path.isfile(image):
            img_path = os.path.join('...', image)
            os.remove(img_path)

    def __str__(self):
        return self.name