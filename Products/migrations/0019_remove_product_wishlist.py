# Generated by Django 4.1.4 on 2023-01-13 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0018_product_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='wishlist',
        ),
    ]
