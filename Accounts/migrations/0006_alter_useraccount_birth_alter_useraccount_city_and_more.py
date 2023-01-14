# Generated by Django 4.1.4 on 2023-01-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_useraccount_avatar_alter_useraccount_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='legal_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='physical_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]