from django.db import models

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class BranchCoord(models.Model):
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, related_name='coord', on_delete=models.CASCADE)

    def __str__(self):
        return self.branch.name

class BranchWorkingHours(models.Model):
    week_day = models.CharField(max_length=200, blank=False)
    hour = models.CharField(max_length=200, blank=False)
    branch = models.ForeignKey(Branch, related_name='working_hours',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.branch.name