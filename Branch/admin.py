from django.contrib import admin
from Branch.models import BranchCoord, Branch, BranchWorkingHours

# Register your models here.

admin.site.register(Branch)
admin.site.register(BranchCoord)
admin.site.register(BranchWorkingHours)