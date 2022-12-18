from django.db import models

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)


class BranchCoord(models.Model):
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, related_name='coord', on_delete=models.CASCADE)


class BranchWorkingHours(models.Model):
    week_day = models.TextField(blank=False)
    hour = models.TextField(blank=False)
    branch = models.ForeignKey(Branch, related_name='working_hours', on_delete=models.CASCADE)