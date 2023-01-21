# Generated by Django 4.1.4 on 2023-01-16 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0007_remove_wishlist_wished_item'),
        ('Products', '0024_remove_product_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wished_product', to='wishlist.wishlist'),
        ),
    ]
