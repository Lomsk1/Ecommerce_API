# Generated by Django 4.1.4 on 2022-12-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeeklySales', '0003_alter_weeklysale_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklysale',
            name='image',
            field=models.ImageField(blank=True, upload_to='./weekly_sale'),
        ),
    ]