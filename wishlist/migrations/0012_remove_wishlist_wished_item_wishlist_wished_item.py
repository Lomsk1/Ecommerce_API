# Generated by Django 4.1.4 on 2023-01-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0026_remove_product_wishlist'),
        ('wishlist', '0011_alter_wishlist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='wished_item',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='wished_item',
            field=models.ManyToManyField(to='Products.product'),
        ),
    ]