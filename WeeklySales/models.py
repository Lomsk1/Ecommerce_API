from django.db import models
import os

# Create your models here.

class WeeklySale(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='./images/weekly_sale')
    deadline = models.DateField(null=True)

    def img_delete(self, image, *args, **kwargs):
        if os.path.isfile(image):
            img_path = os.path.join('...', image)
            os.remove(img_path)

    def __str__(self):
        return self.text