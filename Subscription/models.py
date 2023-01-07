from django.db import models

# Create your models here.


class Subscription(models.Model):
    email = models.EmailField(blank=False, unique=True)

    def __str__(self):
        return self.email