# Generated by Django 4.1.4 on 2023-01-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_useraccount_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='./user'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
