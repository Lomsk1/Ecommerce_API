# Generated by Django 4.1.4 on 2023-01-13 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0015_rename_branch_in_stock_productbranch_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]