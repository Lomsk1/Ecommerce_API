# Generated by Django 4.1.4 on 2022-12-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
