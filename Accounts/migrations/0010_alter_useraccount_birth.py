# Generated by Django 4.1.4 on 2023-01-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_alter_useraccount_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='birth',
            field=models.DateField(blank=True, default='2099-10-10'),
        ),
    ]
