# Generated by Django 4.1.4 on 2022-12-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0006_alter_branch_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchworkinghours',
            name='hour',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branchworkinghours',
            name='week_day',
            field=models.CharField(max_length=200),
        ),
    ]
