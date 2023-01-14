# Generated by Django 4.1.4 on 2023-01-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0013_remove_useraccount_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='./user'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='birth_day',
            field=models.DateField(blank=True, default='2099-10-10'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='legal_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='physical_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
