# Generated by Django 4.1.4 on 2022-12-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_alter_product_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='./products'),
        ),
    ]
