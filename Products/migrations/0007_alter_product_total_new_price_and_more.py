# Generated by Django 4.1.4 on 2022-12-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_alter_product_price_alter_product_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_new_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
